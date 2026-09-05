import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Get API key
api_key=os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

# Create OpenAI client
client=OpenAI(api_key=api_key)

# Send our first request
response = client.responses.create(
    model="gpt-5-mini",
    input="Hello  This is my first AI project. Explain AI automation in one simple sentence."
)
# Print the AI response
print(response.output_text)

