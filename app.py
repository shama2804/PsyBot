from flask import Flask, request, jsonify, render_template
import openai
import json
from config import OPENAI_API_KEY
import os

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# Load base prompt
with open("prompts/base_prompt.txt") as f:
    base_prompt = f.read()

def load_memory():
    try:
        with open("memory.json") as f:
            return json.load(f)
    except:
        return []

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory[-10:], f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    memory = load_memory()
    memory.append({"role": "user", "content": user_input})

    messages = [{"role": "system", "content": base_prompt}] + memory

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.8,
        max_tokens = 150
    )

    reply = response.choices[0].message["content"]
    memory.append({"role": "assistant", "content": reply})
    save_memory(memory)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
