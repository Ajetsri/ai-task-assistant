import requests
import json

url = "http://localhost:11434/api/chat"

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

response = requests.post(url, json=data)

re = response.json()

ai_text = re["message"]["content"]

print("AI response:")
print(ai_text)

task_data = json.loads(ai_text)

print("\nPython object:")
print(task_data)

print("\nAction:")
print(task_data["action"])

print("Task:")
print(task_data["task"])

print("Priority:")
print(task_data["priority"])

print("Due date:")
print(task_data["due_date"])

if task_data["action"] == "create_task":
    print("\n🤖 AI requested task creation!")
    print("Creating task...")