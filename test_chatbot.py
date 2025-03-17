from models.chatbot import ChatBot

def main():
    print("Chatbot Test")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    chatbot = ChatBot()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
        print("-" * 50)

if __name__ == "__main__":
    main() 