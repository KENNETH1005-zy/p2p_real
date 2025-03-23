# storage.py

from security import encrypt_message, decrypt_message

messages = []
subscriptions = {}

def save_message(sender, topic, content):
    encrypted = encrypt_message(topic, content)
    messages.append({
        "from": sender,
        "topic": topic,
        "msg": encrypted
    })

def subscribe_user(username, topic):
    if username not in subscriptions:
        subscriptions[username] = []
    if topic not in subscriptions[username]:
        subscriptions[username].append(topic)

def get_user_subscriptions(username):
    return subscriptions.get(username, [])

def get_messages_for_user(username):
    user_topics = subscriptions.get(username, [])
    user_msgs = [msg for msg in messages if msg["topic"] in user_topics]
    # decrypt each message before returning
    return [{
        "from": msg["from"],
        "topic": msg["topic"],
        "msg": decrypt_message(msg["topic"], msg["msg"])
    } for msg in user_msgs]