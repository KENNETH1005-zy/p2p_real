import requests

# Step 1: Bob subscribes to the topic "news"
res = requests.post("http://127.0.0.1:5000/subscribe", json={
    "user": "Bob",
    "topic": "news"
})
print("[1] Subscribe response:", res.json())

# Step 2: Alice publishes a message to "news"
res = requests.post("http://127.0.0.1:5000/publish", json={
    "from": "Alice",
    "topic": "news",
    "msg": "Breaking news: Python takes over the world!"
})
print("[2] Publish response:", res.json())

# Step 3: Bob retrieves his inbox
res = requests.get("http://127.0.0.1:5000/inbox/Bob")
print("[3] Bob's Inbox:", res.json())

# Step 4: Check Bob's subscriptions
res = requests.get("http://127.0.0.1:5000/subscriptions/Bob")
print("[4] Subscriptions:", res.json())