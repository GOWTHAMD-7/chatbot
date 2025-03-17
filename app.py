from flask import Flask, render_template, request, jsonify
import os
import json
import random
from models.chatbot import ChatBot

app = Flask(__name__, template_folder='templates', static_folder='static')
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'response': 'Please enter a message'})
    
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True) 