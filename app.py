from flask import Flask, render_template, request, jsonify
import os
import json
import random
import traceback
import sys

# Import our custom NLTK setup first
import nltk_setup

# Then import the ChatBot class
from models.chatbot import ChatBot

app = Flask(__name__, template_folder='templates', static_folder='static')

# Initialize the chatbot with error handling
try:
    chatbot = ChatBot()
except Exception as e:
    print(f"Error initializing chatbot: {str(e)}")
    traceback.print_exc()
    # Create a simple fallback chatbot if the main one fails
    class FallbackChatBot:
        def get_response(self, message):
            return "I'm having technical difficulties. Please try again later."
    chatbot = FallbackChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'response': 'Please enter a message'})
        
        bot_response = chatbot.get_response(user_message)
        return jsonify({'response': bot_response})
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        traceback.print_exc()
        return jsonify({'response': 'Sorry, I encountered an error. Please try again.'})

@app.route('/debug', methods=['GET'])
def debug():
    """A debug endpoint to check if the app is running correctly"""
    return jsonify({
        'status': 'ok',
        'python_version': sys.version,
        'env': dict(os.environ),
        'cwd': os.getcwd(),
        'files': os.listdir('.')
    })

# This is for local development
if __name__ == '__main__':
    app.run(debug=True) 