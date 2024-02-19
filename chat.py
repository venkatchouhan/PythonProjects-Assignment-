import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"(.*) your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day.",]
    ],
]

# Create a chatbot using the pairs defined
chatbot = Chat(pairs, reflections)

# Define a function to start the chat
def start_chat():
    print("Hi! I'm Chatbot. How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input.lower() == "quit":
            break

# Start the chat

import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"(.*) your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a great day.",]
    ],
]

# Create a chatbot using the pairs defined
chatbot = Chat(pairs, reflections)

# Define a function to start the chat
def start_chat():
    print("Hi! I'm Chatbot. How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input.lower() == "quit":
            break

# Start the chat
if __name__ == "__main__":
    start_chat()

