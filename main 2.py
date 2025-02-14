import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor

class Character(BaseModel):
    name: str
    fact: List[str] = Field(..., description="A list of facts about the subject")

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

client = instructor.from_groq(client, mode=instructor.Mode.JSON)

# Loop to keep asking questions
while True:
    user_input = input("Ask me about something (or type 'quit' to exit): ")
    if user_input.lower() == "quit":
        print("Exiting...")
        break

    try:
        resp = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides information about various topics.",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            response_model=Character,
        )
        print(resp.model_dump_json(indent=2))
    except Exception as e:
        print(f"An error occurred: {e}")