import requests
import json


# Function to create a task
def create_task(task, priority, due_date):
    print("\n✅ Creating task...")

    print("Task:", task)
    print("Priority:", priority)
    print("Due date:", due_date)

    return {
        "status": "created",
        "task": task,
        "priority": priority,
        "due_date": due_date
    }


# Ollama API endpoint
url = "http://localhost:11434/api/chat"


# Data we are sending to the AI
data = {
    "model": "llama3.2:3b",

    "messages": [
        {
            "role": "system",
            "content": """
You convert user requests into JSON.

Return ONLY valid JSON in exactly this format:

{
    "action": "create_task",
    "task": "task name",
    "priority": "high",
    "due_date": "date"
}

Never add explanations.
"""
        },

        {
            "role": "user",
            "content": "Create a high priority task called Deploy API for tomorrow."
        }
    ],

    "stream": False
}


# Send request to Ollama
response = requests.post(url, json=data)


# Convert Ollama's response from JSON into a Python dictionary
result = response.json()


# Get the AI's actual text response
ai_text = result["message"]["content"]


print("AI response:")
print(ai_text)


# Convert AI's JSON text into a Python dictionary
task_data = json.loads(ai_text)


print("\nPython object:")
print(task_data)


# Read individual values from the Python dictionary
print("\nAction:")
print(task_data["action"])

print("Task:")
print(task_data["task"])

print("Priority:")
print(task_data["priority"])

print("Due date:")
print(task_data["due_date"])


# Decide what Python should do
if task_data["action"] == "create_task":

    result = create_task(
        task_data["task"],
        task_data["priority"],
        task_data["due_date"]
    )

    print("\nFinal result:")
    print(result)