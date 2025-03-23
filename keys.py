# keys.py

from cryptography.fernet import Fernet

topic_keys = {}  # { "topic": Fernet key }

def get_or_create_key(topic):
    if topic not in topic_keys:
        topic_keys[topic] = Fernet(Fernet.generate_key())
    return topic_keys[topic]