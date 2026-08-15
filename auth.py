from helpers import load_json, save_json

USERS_FILE = "data/users.json"

def load_users():
    return load_json(USERS_FILE, {})

def register(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists"
    users[username] = {"password": password}
    save_json(USERS_FILE, users)
    return True, "Registration successful"

def login(username, password):
    users = load_users()
    if username not in users:
        return False, "User not found"
    if users[username]["password"] != password:
        return False, "Incorrect password"
    return True, "Login successful"