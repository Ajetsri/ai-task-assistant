import requests

url="http://localhost:11434/api/generate"

data={
    "model":"llama3.2:3b",
    "prompt":"Explain AI automation in one simple sentence.",
    "stream":False   #Give me the completed response instead of sending it piece-by-piece.
}

response = requests.post(url,json=data)
result = response.json()
print(result["response"])