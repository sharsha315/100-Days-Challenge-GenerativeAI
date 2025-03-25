import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

# Load environment variables from .env file
load_dotenv()

# Initializing Hugging Face TOKEN
HF_TOKEN = os.getenv("HF_TOKEN")

# Model
model_id = "meta-llama/Llama-3.2-3B"

# Using pipeline
pipeline = transformers.pipeline("text-generation",
                                token=HF_TOKEN,
                                model=model_id,
                                model_kwargs={"torch_dtype": torch.bfloat16}, 
                                device_map="auto")

response = pipeline("Hey how are you doing today")
print()
print(response[0]['generated_text'])
