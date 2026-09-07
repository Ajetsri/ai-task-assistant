import requests


url = "http://localhost:3000/api/tasks"


data = {
    "task": "learn spanish",
    "priority": "high"
}


response = requests.post(url, json=data)


print("Status code:")
print(response.status_code)

print("\nResponse:")
print(response.json())