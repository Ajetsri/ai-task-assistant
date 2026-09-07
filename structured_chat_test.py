import requests
import json


# Function that sends the task to our backend API
def create_task(task, priority, due_date):

    url = "http://localhost:3000/api/tasks"

    data = {
        "task": task
    }

    response = requests.post(url, json=data)

    print("\nAPI Status:")
    print(response.status_code)

    print("\nAPI Response:")
    print(response.text)

    return response


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


# Convert Ollama response into Python dictionary
result = response.json()


# Get AI's actual response
ai_text = result["message"]["content"]


print("AI response:")
print(ai_text)


# Convert AI JSON text into Python dictionary
task_data = json.loads(ai_text)


print("\nPython object:")
print(task_data)


# Read AI's decision
print("\nAction:")
print(task_data["action"])

print("Task:")
print(task_data["task"])

print("Priority:")
print(task_data["priority"])

print("Due date:")
print(task_data["due_date"])


# Execute the requested action
if task_data["action"] == "create_task":

    result = create_task(
        task_data["task"],
        task_data["priority"],
        task_data["due_date"]
    )

    print("\nFinal result:")
    print(result.text)