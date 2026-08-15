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

def validate_credentials(username, password):
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(password) < 4:
        return False, "Password must be at least 4 characters"
    return True, "Valid"

def auth_prompt():
    choice = input("1) Login  2) Register: ")
    username = input("Username: ")
    password = input("Password: ")
    if choice == "2":
        valid, msg = validate_credentials(username, password)
        if not valid:
            print(msg); return None
        ok, msg = register(username, password)
    else:
        ok, msg = login(username, password)
    print(msg)
    return username if ok else None