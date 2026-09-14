import requests
import json


# Get request from the user
user_request = input("🤖 What would you like me to do? ")


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

#get task
def get_tasks():

    url = "http://localhost:3000/api/tasks"
    response = requests.get(url)

    print("\nAPI Status:")
    print(response.status_code)

    print("\nAPI Response:")
    print(response.text)

    return response

# Find a task's MongoDB ID using its task name
def find_task_id(task_name):

    url = "http://localhost:3000/api/tasks"

    response = requests.get(url)

    print("\nSearching for task:")
    print(task_name)

    tasks = response.json()["data"]

    for task in tasks:

        if task["task"].lower() == task_name.lower():

            print("\nTask found!")
            print("Task ID:")
            print(task["_id"])

            return task["_id"]

    print("\nTask not found.")

    return None
#complete status change
def complete_task(task_id):
    url=f"http://localhost:3000/api/tasks/{task_id}"
    data = {
        "completed": True
    }

    response = requests.patch(url, json=data)
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
You are a task management assistant.

Your job is to convert the user's request into ONE JSON action.

Available actions:

1. create_task
2. get_tasks
3. complete_task

IMPORTANT RULES:

- If the user asks to create, add, make, or create a task, use create_task.
- If the user asks to show, list, view, or get tasks, use get_tasks.
- If the user asks to complete, finish, mark as completed, or mark done, use complete_task.
- For complete_task, extract ONLY the actual task name.
- Do NOT include words like "mark", "complete", "completed", or "done" in the task name.
- Do NOT invent tasks.
- Do NOT return tasks from examples.
- Return ONLY valid JSON.
- Never add explanations.

For create_task, return:

{
    "action": "create_task",
    "task": "task name",
    "priority": "high",
    "due_date": "date"
}

For get_tasks, return:

{
    "action": "get_tasks"
}

For complete_task, return:

{
    "action": "complete_task",
    "task": "actual task name"
}
"""
        },

        {
            "role": "user",
            "content": user_request
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


print("\nAI response:")
print(ai_text)

ai_text = ai_text.replace("```json", "")
ai_text = ai_text.replace("```", "")
ai_text = ai_text.strip()

# Convert AI JSON text into Python dictionary
task_data = json.loads(ai_text)


print("\nPython object:")
print(task_data)


# Read AI's decision
print("\nAction:")
print(task_data["action"])


# Execute the requested action
if task_data["action"] == "create_task":

    print("Task:")
    print(task_data["task"])

    print("Priority:")
    print(task_data["priority"])

    print("Due date:")
    print(task_data["due_date"])

    result = create_task(
        task_data["task"],
        task_data["priority"],
        task_data["due_date"]
    )

    print("\nFinal result:")
    print(result.text)


elif task_data["action"] == "get_tasks":

    result = get_tasks()

    print("\nFinal result:")
    print(result.text)
elif task_data["action"] == "complete_task":

    print("Task to complete:")
    print(task_data["task"])

    task_id = find_task_id(task_data["task"])

    if task_id:

        result = complete_task(task_id)

        print("\nFinal result:")
        print(result.text)