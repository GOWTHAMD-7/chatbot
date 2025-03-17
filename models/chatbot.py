import random
import json
import os
import nltk
from nltk.stem import WordNetLemmatizer

class ChatBot:
    def __init__(self):
        # Download necessary NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('punkt')
            nltk.download('wordnet')
        
        self.lemmatizer = WordNetLemmatizer()
        
        # Load intents from file if it exists, otherwise use default responses
        self.intents_file = os.path.join(os.path.dirname(__file__), 'intents.json')
        if os.path.exists(self.intents_file):
            with open(self.intents_file, 'r') as f:
                self.intents = json.load(f)
        else:
            # Default intents if file doesn't exist
            self.intents = {
                "intents": [
                    {
                        "tag": "greeting",
                        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
                        "responses": ["Hello!", "Hey there!", "Hi! How can I help you today?"]
                    },
                    {
                        "tag": "goodbye",
                        "patterns": ["Bye", "See you later", "Goodbye", "I'm leaving"],
                        "responses": ["Goodbye!", "See you later!", "Take care!"]
                    },
                    {
                        "tag": "thanks",
                        "patterns": ["Thanks", "Thank you", "That's helpful"],
                        "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
                    },
                    {
                        "tag": "about",
                        "patterns": ["Who are you", "What are you", "Tell me about yourself"],
                        "responses": ["I'm a simple chatbot created to help you!", "I'm your friendly AI assistant."]
                    },
                    {
                        "tag": "help",
                        "patterns": ["Help", "I need help", "Can you help me", "What can you do"],
                        "responses": ["I can answer simple questions and have conversations. What do you need help with?", 
                                     "I'm here to assist you. What would you like to know?"]
                    },
                    {
                        "tag": "fallback",
                        "patterns": [],
                        "responses": ["I'm not sure I understand. Could you rephrase that?", 
                                     "I don't have an answer for that yet.", 
                                     "I'm still learning. Could you try asking something else?"]
                    }
                ]
            }
            # Save default intents
            self._save_intents()
    
    def _save_intents(self):
        """Save the intents to a file"""
        os.makedirs(os.path.dirname(self.intents_file), exist_ok=True)
        with open(self.intents_file, 'w') as f:
            json.dump(self.intents, f, indent=4)
    
    def _preprocess(self, sentence):
        """Tokenize and lemmatize the sentence"""
        words = nltk.word_tokenize(sentence.lower())
        return [self.lemmatizer.lemmatize(word) for word in words]
    
    def _pattern_match(self, message):
        """Simple pattern matching to find the best intent match"""
        best_match = {"tag": "fallback", "score": 0}
        
        processed_message = set(self._preprocess(message))
        
        for intent in self.intents["intents"]:
            score = 0
            for pattern in intent["patterns"]:
                pattern_words = set(self._preprocess(pattern))
                # Calculate simple overlap score
                if pattern_words and processed_message:
                    overlap = len(pattern_words.intersection(processed_message))
                    pattern_score = overlap / len(pattern_words)
                    score = max(score, pattern_score)
            
            if score > best_match["score"] and score > 0.5:  # Threshold for matching
                best_match = {"tag": intent["tag"], "score": score}
        
        return best_match["tag"]
    
    def get_response(self, message):
        """Generate a response based on the user's message"""
        tag = self._pattern_match(message)
        
        # Find the matching intent
        for intent in self.intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        
        # Fallback response if no match found
        fallback_responses = ["I'm not sure I understand.", "Could you rephrase that?", "I don't have an answer for that yet."]
        return random.choice(fallback_responses)
    
    def add_intent(self, tag, patterns, responses):
        """Add a new intent or update an existing one"""
        # Check if intent already exists
        for intent in self.intents["intents"]:
            if intent["tag"] == tag:
                intent["patterns"].extend(patterns)
                intent["responses"].extend(responses)
                self._save_intents()
                return True
        
        # Create new intent
        new_intent = {
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        }
        self.intents["intents"].append(new_intent)
        self._save_intents()
        return True 