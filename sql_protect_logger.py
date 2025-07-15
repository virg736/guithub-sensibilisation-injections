import sqlite3
import hashlib

# Connexion à la base de données
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Simuler des entrées utilisateur (remplacer par input si besoin)
username = "admin"
password = "password123"

# Requête sécurisée
hash_pw = hashlib.sha256(password.encode()).hexdigest()
cur.execute(
    "SELECT * FROM users WHERE username = ? AND password_hash = ?",
    (username, hash_pw)
)
user = cur.fetchone()

if user:
    print("✅ Connexion réussie.")
else:
    print("❌ Identifiants invalides.")

# Logs de détection
cur.execute("SELECT * FROM logs")
logs = cur.fetchall()

if logs:
    print("\n🚨 Logs de tentatives détectées :")
    for log in logs:
        print(
            "IP: {} | User: {} | Payload: {}".format(
                log[1], log[2], log[4]
            )
        )

conn.close()
