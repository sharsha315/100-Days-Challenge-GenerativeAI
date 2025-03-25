import os
from dotenv import load_dotenv
import cohere

# Load environmental variables from .env file
load_dotenv()

# Get the cohere api key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Create the client
client = cohere.ClientV2(COHERE_API_KEY)

# Generate text
response = client.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Explain Deep Learning in one-sentence",
        }
    ],
)

print()
print(response.message.content[0].text)
print()