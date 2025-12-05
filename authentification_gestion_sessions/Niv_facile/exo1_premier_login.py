
USERNAME = "admin"
PASSWORD = "password123"

username_input = input("Nom d'utilisateur : ")
password_input = input("Mot de passe : ")

if username_input == USERNAME and password_input == PASSWORD:
    print("Connexion réussie")
else:
    print("Échec")
