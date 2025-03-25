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

# Define the model prompt and model id
prompt = "Write a Hello World function in Python programming language"

model_id = "amazon.titan-text-express-v1"

# Configure inference parameters
inference_parameters = {
   "inputText": prompt,
   "textGenerationConfig": {
       "maxTokenCount": 512,  # Limit the response length
       "temperature": 0.1,    # Control the randomness of the output
   },
}

# Convert the request payload to JSON
request_payload = json.dumps(inference_parameters)

# Invoke the model
response = client.invoke_model(
    modelId=model_id,
    body=request_payload,
    contentType="application/json",
    accept="application/json"
)

# Decode the response body
response_body = json.loads(response["body"].read())

# Extract and print the generated text
generated_text = response_body["results"][0]["outputText"]
print("Generated Text:\n", generated_text)
