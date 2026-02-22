import nltk
import string
from nltk.chat.util import Chat, reflections

# -------- Text Preprocessing Function --------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# -------- Chat Patterns --------
pairs = [

    [r"hi|hello|hey",
     ["Hello 👋", "Hey there 😊", "Hi! How can I help you today?"]],

    [r"how are you",
     ["I'm doing great! How about you? 😊"]],

    [r"i am fine|i am good",
     ["Nice to hear that 😄 How can I help you?"]],

    [r"what is your name",
     ["I am Harshi's Chatbot 🤖"]],

    [r"who created you",
     ["I was created by Harshita Goud during CODTECH internship 💻"]],

    [r"what can you do",
     ["I can chat with you, answer questions and tell jokes 😄"]],

    [r"tell me a joke",
     ["Why do programmers hate nature? Too many bugs 😂"]],

    [r"what is python",
     ["Python is a popular programming language used for AI, ML and automation."]],

    [r"what is ai",
     ["AI means Artificial Intelligence — machines that can think like humans 🤖"]],

    [r"what is internship",
     ["Internship is a training program that gives real work experience."]],

    [r"thank you|thanks",
     ["You're welcome 😊", "Happy to help!"]],

    [r"bye|goodbye|exit",
     ["Goodbye 👋 Have a great day!", "Bye! Take care 😄"]]
]

# -------- Create Chatbot --------
chatbot = Chat(pairs, reflections)

print("Harshi's Chatbot 🤖 (type 'exit' to quit)")

# -------- Chat Loop --------
while True:
    user_input = input("You: ")
    user_input = clean_text(user_input)

    if user_input == "exit":
        print("Chatbot: Goodbye 👋")
        break

    response = chatbot.respond(user_input)

    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: Sorry, I don't understand that yet 😅")
