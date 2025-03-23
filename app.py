# app.py

from flask import Flask, request, jsonify
from storage import (
    save_message,
    get_messages_for_user,
    subscribe_user,
    get_user_subscriptions
)

app = Flask(__name__)

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()
    username = data.get("user")
    topic = data.get("topic")
    subscribe_user(username, topic)
    return jsonify({"status": f"{username} subscribed to {topic}"})

@app.route("/publish", methods=["POST"])
def publish():
    data = request.get_json()
    sender = data.get("from")
    topic = data.get("topic")
    content = data.get("msg")
    save_message(sender, topic, content)
    return jsonify({"status": "message published"})

@app.route("/inbox/<username>", methods=["GET"])
def get_inbox(username):
    msgs = get_messages_for_user(username)
    return jsonify(msgs)

@app.route("/subscriptions/<username>", methods=["GET"])
def get_subscriptions(username):
    return jsonify(get_user_subscriptions(username))

if __name__ == "__main__":
    app.run(port=5000)