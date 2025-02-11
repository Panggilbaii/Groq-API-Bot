import requests
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# API Endpoint
API_URL = "https://api.groq.com/v1/chat/completions"

# Function to interact with Groq API
def get_groq_response(question):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "groq-chat-model",  # Replace with actual model name
        "messages": [{"role": "user", "content": question}]
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to fetch response from Groq API."

# Main loop
if __name__ == "__main__":
    print("Welcome to Groq AI Chat! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        answer = get_groq_response(user_input)
        print("Groq AI:", answer)
