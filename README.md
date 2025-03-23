# 🔄 P2P Messaging System with Pub-Sub & Encryption

This project is a Python-based peer-to-peer messaging system built with Flask. It supports direct messaging, topic-based publish-subscribe messaging, and encrypted communication using symmetric keys. 

---

## ✅ Features

- Phase 1: Socket-based peer-to-peer chat system (see `client.py`, `server.py`)
- Phase 2: RESTful API for messaging (Flask)
- Phase 3: Topic-based publish-subscribe system
- Phase 4: End-to-end encryption using AES (Fernet)
- Local in-memory storage, no centralized cloud backend
- Topic-specific encryption keys
- Designed to simulate secure, distributed messaging environments

---

## 📁 Project Structure

```
p2p_real/
├── app.py              # Flask server providing messaging APIs
├── storage.py          # Manages message storing and subscriptions
├── security.py         # Handles encryption and decryption
├── keys.py             # Generates and stores keys for each topic
├── test_requests.py    # Basic API messaging test
├── pubsub_requests.py  # Full publish-subscribe flow test
├── client.py           # (Phase 1) Socket-based client
├── server.py           # (Phase 1) Socket-based server
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository or copy the files:

```bash
cd p2p_real/
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # On macOS/Linux
# OR
.venv\Scripts\activate        # On Windows
```

3. Install required dependencies:

```bash
pip install flask requests cryptography
```

---

## 🚀 Running the Project

### 1. Start the Flask API Server

Run this in one terminal:

```bash
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

This server handles all message sending, inbox retrieval, subscription management, and encryption.

---

### 2. Test the Pub-Sub Flow

Open a second terminal and run:

```bash
python pubsub_requests.py
```

This script:

- Subscribes user "Bob" to topic `"news"`
- Publishes a message to `"news"` from user "Alice"
- Retrieves Bob's inbox
- Verifies Bob’s active subscriptions

Expected output:

```
[1] Subscribe response: {'status': 'Bob subscribed to news'}
[2] Publish response: {'status': 'message published'}
[3] Bob's Inbox: [{'from': 'Alice', 'topic': 'news', 'msg': '...'}]
[4] Subscriptions: ['news']
```

The message is encrypted in storage and decrypted automatically when retrieved.

---

## 🔐 Security Model

- All messages are encrypted using symmetric AES encryption (Fernet)
- Each topic has its own encryption key (generated automatically)
- Messages are decrypted only when users retrieve their inbox
- No messages are stored in plaintext

---

## 🧪 Additional Testing

To simulate raw API behavior, run `test_requests.py` or use `curl` or Postman to interact with:

- `POST /subscribe` → subscribe a user to a topic
- `POST /publish` → publish a message to a topic
- `GET /inbox/<username>` → retrieve decrypted messages for a user
- `GET /subscriptions/<username>` → check which topics a user is subscribed to

---





## 🧠 Author

Zhengyuan Li  
EC530 – Secure P2P Messaging Project
