from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS to allow frontend requests

app = Flask(__name__)
CORS(app)  # Allow all cross-origin requests

# Dictionary of predefined responses
responses = {
    # Greetings
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "hey": "Hey! How’s your day going?",
    "good morning": "Good morning! Have a great day!",
    "good afternoon": "Good afternoon! How can I assist?",
    "good evening": "Good evening! What’s up?",

    # Common Questions
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot, your virtual assistant!",
    "who created you": "I was created by a developer who loves coding!",
    "what can you do": "I can chat with you, answer questions, and make your day better!",
    "where are you from": "I'm from the digital world, floating in the cloud!",
    "how old are you": "I'm as old as the internet itself... or maybe just a few minutes old!",
    
    # Feelings & Emotions
    "i am happy": "That’s awesome! Keep smiling 😊",
    "i am sad": "Oh no! I’m here to cheer you up. What’s wrong?",
    "i am tired": "Take a break and rest! You deserve it.",
    "i am bored": "Let's play a game or chat about something interesting!",
    "i am excited": "Yay! What’s making you so excited?",
    
    # Fun Questions
    "tell me a joke": "Sure! Why don't skeletons fight each other? Because they don't have the guts! 😂",
    "tell me a riddle": "Alright! What has keys but can't open locks? ... A piano!",
    "sing me a song": "I wish I could, but I can hum... hmm hmm 🎶",
    "do you like music": "Yes! I love music, especially AI-generated beats!",
    "what is your favorite color": "I like all colors, but blue is cool!",
    
    # Technology & Knowledge
    "what is ai": "AI stands for Artificial Intelligence. It helps machines think and learn like humans.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn from data.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "who is the president of usa": "As of 2025, it's Joe Biden. But you might want to check the latest updates!",
    "how does the internet work": "The internet is a global network that connects millions of computers together.",
    
    # Personal Questions
    "do you have a family": "Not exactly, but I have a lot of friends like you!",
    "are you a robot": "Yes, I am a chatbot, but I love talking like a human!",
    "can you feel emotions": "I can understand emotions, but I don’t feel them like humans do.",
    "do you sleep": "Nope! I’m always here for you 24/7!",
    "do you have a hobby": "Chatting with you is my favorite hobby!",
    
    # Advice & Motivation
    "give me a motivation quote": "Sure! 'Believe you can, and you’re halfway there.'",
    "how to stay positive": "Focus on the good things, surround yourself with positivity, and keep moving forward!",
    "how to focus on studies": "Avoid distractions, make a schedule, and take breaks to stay fresh!",
    "how to stop procrastinating": "Break tasks into small steps and just start! Action beats hesitation.",
    "how to stay healthy": "Eat well, exercise, sleep enough, and drink plenty of water.",
    
    # Random Topics
    "do you believe in aliens": "Maybe! The universe is too big for us to be alone.",
    "what is the meaning of life": "That’s a deep question! Maybe to love, learn, and explore.",
    "who is your favorite superhero": "I like Iron Man! Smart, innovative, and a genius!",
    "which is the best programming language": "It depends! Python is great for AI, JavaScript for web, and C++ for speed.",
    "can you tell the future": "I wish I could! But I can guess… You will have an amazing day! 😊",
    
    # End Conversation
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you next time! Take care!",
    "see you later": "See you soon! Have fun!",
    
    # Default response
    "default": "I'm not sure how to respond to that. Can you ask something else?"
}

# Route for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()
    bot_response = responses.get(user_message, responses["default"])
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
