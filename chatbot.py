# chatbot.py

import nltk
from nltk.chat.util import Chat, reflections

# Download the punkt package for tokenization
nltk.download('punkt')

# Define chatbot responses
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I help you today?']),
    (r'What is your name?', ['I am a chatbot created by your intern project.']),
    (r'How are you?', ['I am just a program, but I am doing fine!']),
    (r'(.*)(help|assist)(.*)', ['I can help you with general information or tasks. What do you need help with?']),
    (r'Quit', ['Goodbye! Have a great day!'])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
def start_chat():
    print("Hello! I'm your chatbot. Type 'Quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
