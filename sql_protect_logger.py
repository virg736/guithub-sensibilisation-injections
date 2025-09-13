#!/usr/bin/env python3
# sql_protect_logger.py – Exemple de protection contre injections SQL
# Copyright (c) 2025 Virginie Lechene
# SPDX-License-Identifier: MIT
# Voir le fichier LICENSE pour plus de détails.
#
# ⚠️ Usage pédagogique uniquement.
# L’auteure décline toute responsabilité en cas d’usage malveillant ou illégal.

import sqlite3
import bcrypt

# Connexion à la base de données
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Simuler des entrées utilisateur (à remplacer par input si besoin)
username = "admin"
password = "password123"

# Générer un hash sécurisé avec bcrypt (si tu veux stocker un nouveau mot de passe)
hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Vérification sécurisée (comparaison entre le mot de passe entré et celui stocké en BDD)
cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
row = cur.fetchone()

if row and bcrypt.checkpw(password.encode(), row[0].encode()):
    print("✅ Connexion réussie.")
else:
    print("❌ Identifiants invalides.")

# Logs de détection
cur.execute("SELECT * FROM logs")
logs = cur.fetchall()

if logs:
    print("\n🚨 Logs de tentatives détectées :")
    for log in logs:
        print("IP: {} | User: {} | Payload: {}".format(log[1], log[2], log[4]))

conn.close()
