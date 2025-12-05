import secrets

USERNAME = "admin"
PASSWORD = "password123"

sessions = {}  

def login(username_input, password_input):
    if username_input == USERNAME and password_input == PASSWORD:
        token = secrets.token_hex(16)     
        sessions[token] = username_input  
        print("Connexion réussie")
        print("Token :", token)
        return token
    else:
        print("Échec")
        return None

def is_logged_in(token):
    return token in sessions

user = input("Nom d'utilisateur : ")
pwd = input("Mot de passe : ")

token = login(user, pwd)

if token:
    print("\nTest d'accès avec token...")
    if is_logged_in(token):
        print("Accès autorisé : utilisateur connecté ->", sessions[token])
    else:
        print("Accès refusé : token invalide")
