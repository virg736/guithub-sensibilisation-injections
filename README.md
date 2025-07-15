# Sensibilisation aux Injections SQL, XSS, etc.

Script Python pédagogique pour détecter et bloquer des tentatives d'injection.
Exemples réels (simulés) et protections intégrées.

---

## Sommaire

- Avertissement
- Objectif
- Fonctionnement global
- Cas d’usage
- Exemples d’injection
- Script de protection intégré
- Prérequis
- Captures d’écran
- Licence
- À propos de l’usage
- Droits sur les visuels

---

## Avertissement

Usage strictement pédagogique.
L’auteure décline toute responsabilité en cas d’utilisation malveillante ou illégale.

---

## Objectif

Fournir une méthode simple pour :

- Comprendre les risques liés aux injections (SQL, XSS, etc.)
- Identifier les vecteurs d’attaque classiques
- Expérimenter un script Python de protection
- Sensibiliser dans un cadre légal et sécurisé

---

## Fonctionnement global

- Le script intercepte les saisies utilisateurs
- Détecte les schémas malveillants (via regex et blacklist)
- Enregistre les tentatives dans une base SQLite
- Fournit un retour neutre type “Identifiants invalides”
- Ne divulgue aucune information technique en cas d’échec

---

## Cas d’usage

Ce script peut être utilisé dans le cadre :

- de démonstrations pédagogiques
- de formations en cybersécurité
- d’exercices de sensibilisation
- d’expérimentations en environnements fermés

---

## Exemples d’injection

🔹 **Exemple 1** :
URL avec injection SQL simulée
`https://site.com/page?id=1' OR '1'='1 --`

🔹 **Exemple 2** :
Formulaire de connexion
- Nom d'utilisateur : `admin' --`
- Mot de passe : *(vide)*

Requête générée (non sécurisée) :

```sql
SELECT * FROM users WHERE username='admin' --' AND password='...';
