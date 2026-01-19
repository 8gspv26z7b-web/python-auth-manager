import hashlib
import sqlite3

class AuthManager:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

    def _hash_pw(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        hashed = self._hash_pw(password)
        try:
            self.cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def login(self, username, password):
        hashed = self._hash_pw(password)
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed))
        return self.cursor.fetchone() is not None

