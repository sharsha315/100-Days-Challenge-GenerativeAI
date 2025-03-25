import os
from dotenv import load_dotenv
import boto3
import json

# Load environmental variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

# Create a Bedrock client
client = boto3.client(
    service_name='bedrock-runtime',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1"
)

body = json.dumps({
  "max_tokens": 256,
  "messages": [{"role": "user", "content": "Hello, world"}],
  "anthropic_version": "bedrock-2023-05-31"
})

response = client.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0")

response_body = json.loads(response.get("body").read())
generated_text = response_body.get("content")[0]["text"]

print()
print(generated_text)
print()