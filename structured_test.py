import requests
import json

url="http://localhost:11434/api/generate"
prompt = """
Convert the following user request into JSON.

User request:
Create a high priority task called Deploy API for tomorrow.

Return ONLY valid JSON with these fields:
action
task
priority
due_date
"""
data = {
    "model":"llama3.2:3b",
    "prompt": prompt,
    "stream":False
}
response = requests.post(url,json=data)
result=response.json()
ai_text=result["response"]
print(ai_text)
