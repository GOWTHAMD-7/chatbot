# Simple Chatbot

A simple chatbot application built with Python Flask and basic NLP techniques.

## Features

- Web-based chat interface
- Pattern matching for understanding user queries
- Customizable responses through intents.json
- Responsive design that works on desktop and mobile

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files

2. Navigate to the project directory:

   ```
   cd chatbot
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Customizing the Chatbot

You can customize the chatbot's responses by editing the `models/intents.json` file. The file contains patterns (what the user might say) and responses (what the chatbot should reply).

Each intent has:

- A tag (category)
- Patterns (example user inputs)
- Responses (possible chatbot replies)

Example:

```json
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Hey"],
  "responses": ["Hello!", "Hi there!", "Hey! How can I help?"]
}
```

## Extending the Chatbot

To make the chatbot smarter, you can:

1. Add more intents to `intents.json`
2. Implement more advanced NLP techniques in the `ChatBot` class
3. Connect to external APIs for real-time data (weather, news, etc.)
4. Add a database to store conversation history

## Project Structure

```
chatbot/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── models/
│   ├── chatbot.py          # ChatBot class implementation
│   └── intents.json        # Conversation patterns and responses
├── static/
│   ├── css/
│   │   └── style.css       # Styling for the chat interface
│   └── js/
│       └── script.js       # Frontend JavaScript for the chat
└── templates/
    └── index.html          # HTML template for the chat interface
```

## License

This project is open source and available under the MIT License.

## Acknowledgements

- Flask - Web framework
- NLTK - Natural Language Processing toolkit
