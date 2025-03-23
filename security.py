# security.py

from keys import get_or_create_key

def encrypt_message(topic, message):
    key = get_or_create_key(topic)
    encrypted = key.encrypt(message.encode())
    return encrypted.decode()  # return as string

def decrypt_message(topic, encrypted_message):
    key = get_or_create_key(topic)
    decrypted = key.decrypt(encrypted_message.encode())
    return decrypted.decode()