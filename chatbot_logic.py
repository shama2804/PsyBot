# chatbot_logic.py

def generate_reply(message):
    """
    Very basic chatbot logic for now.
    You can later plug in NLP/ML models here.
    """
    message = message.lower()

    # Example simple responses
    if "hello" in message or "hi" in message:
        return "Hello there! How are you feeling today?"
    elif "sad" in message:
        return "I'm sorry you're feeling sad. Do you want to talk about it?"
    elif "anxious" in message:
        return "It's okay to feel anxious. I'm here for you."
    elif "thank you" in message:
        return "You're welcome! I'm glad to help 😊"
    elif "bye" in message:
        return "Take care! Remember, I'm always here if you need me."
    else:
        return "I'm here to listen. Tell me more about how you're feeling."
