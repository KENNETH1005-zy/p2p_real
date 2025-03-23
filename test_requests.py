import requests

# Send a message from Alice to Bob using the /publish route
res = requests.post("http://127.0.0.1:5000/publish", json={
    "from": "Alice",
    "topic": "general",
    "msg": "Hello Bob, are you there?"
})
print("Send raw response:", res.text)

# Get Bob's inbox (assuming he is subscribed to "general")
res = requests.get("http://127.0.0.1:5000/inbox/Bob")
print("Bob's Inbox:", res.json())