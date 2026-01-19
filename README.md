# User Authentication Manager (Python)

A secure, lightweight Python module for managing user registration and login flows using SQLite and SHA-256 password hashing.

## 🛠 Features
- **Persistent Storage:** Uses SQLite for local database management.
- **Security First:** Implements SHA-256 hashing (no plain-text passwords).
- **Clean Logic:** Encapsulated class-based structure for easy integration.

## 🚀 Usage

### 1. Initialization
```python
from auth_manager import AuthManager
auth = AuthManager("my_database.db")
auth.register_user("Mark_Admin", "secure_password123")
if auth.login("Mark_Admin", "secure_password123"):
    print("Access Granted")
