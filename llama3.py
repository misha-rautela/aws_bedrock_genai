#Code to call llama3 model in bedrock without using lambda function and getting the GENAI feedback

#import boto3 for connection to bedrock
import boto3
#import json for response format
import json

# Define prompt to be passed to the model
prompt_data="""
Act as a famous poet Elizabeth Cary and write a poem on batman
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt":prompt_data,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
model_id="meta.llama3-8b-instruct-v1:0"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)
