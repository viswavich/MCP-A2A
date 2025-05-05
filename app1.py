# app1_sender.py
import requests

data = {
    "id": 101,
    "message": "Hello from App1"
}

response = requests.post("http://127.0.0.1:5000/receive", json=data)

print("[Sender] Server Response:", response.json())