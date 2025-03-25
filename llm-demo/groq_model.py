import os
from dotenv import load_dotenv
from groq import Groq

# Load environmental variables from .env file
load_dotenv()

# Get the cohere api key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq()

# Generate response
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "What is LLM finetuning? Answer in a sentence"
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

print()
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
print()