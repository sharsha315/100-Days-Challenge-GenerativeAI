import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables from .env file
load_dotenv()

# Initializing Hugging Face TOKEN
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

model = "mistral-large-latest"

client = Mistral(api_key=MISTRAL_API_KEY)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What are LLMs? Give me a one line answer.",
        },
    ]
)

print()
print(chat_response.choices[0].message.content)
print()
