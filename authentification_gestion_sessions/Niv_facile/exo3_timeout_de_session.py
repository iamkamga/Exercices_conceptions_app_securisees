 import secrets
import time

USERNAME = "admin"
PASSWORD = "password123"

sessions = {}

SESSION_DURATION = 5 * 60  

def cleanup_expired_sessions():
    """Supprime les sessions expirées."""
    now = time.time()
    expired = []

    for token, data in sessions.items():
        if now - data["created_at"] > SESSION_DURATION:
            expired.append(token)

    for token in expired:
        del sessions[token]

def login(username_input, password_input):
    """Login simple avec création d'une session."""
    cleanup_expired_sessions()

    if username_input == USERNAME and password_input == PASSWORD:
        token = secrets.token_hex(16)
        sessions[token] = {
            "username": username_input,
            "created_at": time.time()
        }
        print("Connexion réussie")
        print("Token :", token)
        return token

    print("Échec")
    return None

def is_logged_in(token):
    """Vérifie si le token est valide et non expiré."""
    cleanup_expired_sessions()

    if token in sessions:
        return True
    return False


print("=== Connexions simultanées ===")
t1 = login("admin", "password123")
time.sleep(1)
t2 = login("admin", "password123")
time.sleep(1)
t3 = login("admin", "password123")

print("\nSessions actives initialement :")
print(sessions)

print("\nVérification de chaque token :")
for t in [t1, t2, t3]:
    print("Token", t[:6], "... ->", "OK" if is_logged_in(t) else "EXPIRÉ")

print("\nSimulation d’expiration : attente de 6 minutes...")
time.sleep(6 * 60)

cleanup_expired_sessions()

print("\nSessions après expiration :")
print(sessions)
