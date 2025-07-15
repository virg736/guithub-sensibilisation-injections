# guithub-sensibilisation-injections

# 🛡️ Sensibilisation aux injections SQL

---

## ⚠️ À propos

Ce projet vise à **sensibiliser aux failles d’injection** (notamment SQL), en expliquant les risques, les vecteurs d’attaque, et en présentant un **script de protection fonctionnel écrit en Python**.

> ⚠️ **Les exemples d’injection sont fictifs ou neutralisés.**
>
> ✅ **Le script de protection, lui, est réel et opérationnel** — il utilise de vraies requêtes préparées, un hachage sécurisé, et une détection de patterns d’injection.

---

## 🎯 Objectif

Proposer un **exemple fonctionnel de protection contre les injections**, avec :
- un script Python réel et exécutable
- un système de détection de payloads malveillants
- une base de données SQLite simulée
- des logs pour analyser les tentatives

Ce projet est idéal pour :
- les formations en cybersécurité
- les démonstrations d’audit applicatif
- les étudiants ou passionnés de sécurité

---

## 🔎 Qu’est-ce qu’une injection ?

Une injection est une faille qui permet à un attaquant d’introduire du **code externe non filtré** dans une requête exécutée par l’application (ex : SQL, HTML, système…).

Elle peut entraîner :
- Vol de données
- Contournement d’authentification
-  Modification ou suppression de données
- ⚠️ Prise de contrôle d’un système

---

##  Types d’injection présentés

| Type | Description |
|---------------------|----------------------------------------------|
| **SQL Injection** | Code SQL injecté dans une requête |
| **XSS** | HTML ou JS injecté dans une page web |
| **Command Injection** | Commandes système exécutées via une entrée |
| **LDAP Injection** | Requête LDAP manipulée |
| **Header Injection**| En-têtes HTTP corrompus |

---

## 📍 Où les injections peuvent-elles se produire ?

- Paramètres GET (`?id=1`)
- Champs de formulaire (`login`, `search`, etc.)
- Cookies (`session=...`)
- En-têtes HTTP (`User-Agent`, `Referer`)
- Corps de requêtes POST
- Interfaces non protégées

---

##  Exemples d’injection fictive

**Exemple 1 – URL**
``https://site.com/page?id=1' OR '1'='1 --``

**Exemple 2 – Formulaire de login**
Nom d'utilisateur : `admin' --`
Mot de passe : *(vide)*

Requête générée :
```sql
SELECT * FROM users WHERE username='admin' --' AND password='...';


##  Limitations


🛑 Ce script n’est pas adapté pour une application en production.


En environnement réel, il faut :

utiliser un framework sécurisé (Django, Flask avec ORM…)

mettre en place une politique d’authentification forte (MFA, rate limiting…)

stocker les logs de façon centralisée

intégrer une détection d’intrusion (WAF, SIEM…)

📸 Démonstration


Des captures d’écran d’exécution sont incluses dans le dossier /screenshots/.

📄 Licence


Projet sous licence MIT – Usage libre à but éducatif.

Créé  pour la sensibilisation à la cybersécurité.





