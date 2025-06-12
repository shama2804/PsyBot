from flask import Flask, render_template, request, jsonify
from chatbot_logic import generate_reply

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    reply = generate_reply(message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
