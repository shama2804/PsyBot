from sentence_transformers import SentenceTransformer, util

# Pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Custom training examples (expand this as you go)
training_data = [
    {"input": "I feel nervous about an interview", "response": "It’s normal to feel nervous. Let’s practice some calming techniques together."},
    {"input": "I’m feeling down today", "response": "I’m sorry you’re feeling down. Want to share what’s on your mind?"},
    {"input": "I’m lonely even when I’m with people", "response": "That sounds really tough. I’m here to listen whenever you need."},
    {"input": "I’m scared of failing", "response": "Fear of failure is common. Remember, it’s part of learning and growing."},
    {"input": "I feel like crying but can’t", "response": "Sometimes emotions get stuck. It’s okay, I’m here to support you."},
    {"input": "I’m worried about my family", "response": "Family concerns can be heavy. Want to talk about what’s worrying you?"},
    {"input": "I feel disconnected from everyone", "response": "Feeling disconnected is hard. You’re not alone, and I’m here with you."},
    {"input": "I’m frustrated with myself", "response": "Being hard on yourself happens. Let’s focus on the progress you’ve made."},
    {"input": "I don’t feel motivated", "response": "Motivation can come and go. Want to try some small goals together?"},
    {"input": "I feel like nobody cares", "response": "I care, and I’m here to listen anytime you want to talk."},
    {"input": "I’m anxious about a deadline", "response": "Deadlines can be stressful. Want some tips to manage your time?"}, 
    {"input": "I’m feeling grateful for my friends", "response": "That’s beautiful! Friends can be a great support."},
    {"input": "I’m feeling confused about my future", "response": "The future can feel uncertain. Let’s take it step by step."},
    {"input": "I’m feeling hopeless about everything", "response": "I’m really sorry you’re feeling this way. You don’t have to go through this alone."},
    {"input": "I want to feel calm", "response": "Let’s try a relaxation exercise together."},
    {"input": "I’m angry at someone", "response": "It’s okay to feel angry. Want to talk about what happened?"},
    {"input": "I’m worried I’m not good enough", "response": "You are enough just as you are. Let’s explore these feelings."},
    {"input": "I’m feeling restless", "response": "Restlessness can be tough. How about a quick mindfulness exercise?"},
    {"input": "I feel overwhelmed with work", "response": "Work stress can pile up. Want help organizing your tasks?"}, 
    {"input": "I’m feeling hopeful about a new opportunity", "response": "That’s exciting! What’s making you feel hopeful?"},
    {"input": "I feel like giving up on my goals", "response": "It’s normal to feel that way sometimes. I’m here to support you."},
    {"input": "I’m feeling anxious and can’t concentrate", "response": "That sounds hard. Let’s try a grounding technique together."},
    {"input": "I’m struggling to stay positive", "response": "It’s okay to struggle. Small steps can make a difference."},
    {"input": "I’m scared of being judged", "response": "Fear of judgment is common. You’re safe here with me."},
    {"input": "I’m feeling guilty about something", "response": "Guilt can weigh heavy. Want to talk about it?"},
    {"input": "Shall I share what is wrong", "response": "Of course. I’m here to listen whenever you're ready."},
    {"input": "I want to share what happened", "response": "Please go ahead. I'm listening with care."},
    {"input": "Can I share something with you?", "response": "Yes, absolutely. I’m here for you."},
    {"input": "Can I tell you what happened?", "response": "Of course. I'm here to listen."},
    {"input": "Is it okay if I talk?", "response": "Yes, take your time. I'm right here with you."}

]

conversation_history = []

# Encode all input sentences
input_texts = [item['input'] for item in training_data]
input_embeddings = model.encode([item["input"] for item in training_data], convert_to_tensor=True)

def generate_reply(user_input):
    global conversation_history
    conversation_history.append(user_input)

    # Context-aware short-term memory logic
    if len(conversation_history) >= 2:
        last_msg = conversation_history[-2].lower()
        current_msg = user_input.lower()

        follow_up_intents = [
            "can i share", "can i tell", "shall i tell", "shall i share", "can i talk"
        ]
        if any(phrase in last_msg for phrase in follow_up_intents) and current_msg in ["yes", "yeah", "sure", "go ahead"]:
            return "Go ahead, I’m listening."

        if current_msg in ["no let me share", "first let me share"]:
            return "Sure, take your time. I’m listening."

    # Fallback: semantic similarity
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.cos_sim(user_embedding, input_embeddings)[0]
    best_match_idx = similarities.argmax()
    return training_data[best_match_idx]['response']


# === Example Chat Session ===
if __name__ == "__main__":
    print("🤖 PsyBot: Hi, I’m here for you. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🤖 PsyBot: Take care. I'm here whenever you need me.")
            break
        reply = generate_reply(user_input)
        print(f"🤖 PsyBot: {reply}")
