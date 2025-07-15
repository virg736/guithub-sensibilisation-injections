# 🛡️ Sensibilisation aux Injections SQL & XSS – Projet éducatif Python


📑 Sommaire :
- [Avertissement](#avertissement)
- [Objectif](#objectif)
- [Fonctionnement du script](#fonctionnement-du-script)
- [Captures d’écran](#captures-décran)
- [Exemples d'injection](#exemples-dinjection)
- [Protection intégrée](#protection-intégrée)
- [Limitations & Bonnes pratiques](#limitations--bonnes-pratiques)
- [Licence](#licence)

Sections recommandées :


✋ Avertissement


🛑 Usage strictement pédagogique
Ce projet est conçu à des fins de démonstration. L’auteure décline toute responsabilité en cas d’usage malveillant.
🎯 Objectif


Fournir un exemple clair d’injections SQL/XSS et de leur détection, pour :
Sensibiliser aux attaques web
Montrer l’impact en environnement simulé
Fournir un script Python avec détection d’injections
⚙️ Fonctionnement du script


Le script Python utilise :
Requêtes préparées
Hachage SHA-256 des mots de passe
Détection de patterns d’injection (' OR 1=1, <script>, etc.)
Journalisation des tentatives malveillantes dans une base SQLite


💣 Exemples d’injection
- URL : `http://site.com/page?id=1' OR '1'='1`
- Formulaire :
Nom d'utilisateur : `admin' --`
Mot de passe : *(vide)*
→ Résultat : contournement de l’authentification

**Requête simulée :**
```sql
SELECT * FROM users WHERE username='admin' -- ' AND password='...';


---

#### 🛡️ Protection intégrée

> ✅ Le script bloque automatiquement :
> - Les requêtes malicieuses
> - Enregistre les tentatives
> - Fournit un retour utilisateur neutre : *“Identifiants invalides”*

---

#### ⚠️ Limitations & Bonnes pratiques

> 🚫 Ce script **n’est pas adapté à un environnement de production**.

🔐 En entreprise, il faut :
- Utiliser un **framework sécurisé** (Django, Flask...)
- Appliquer des politiques MFA + rate limiting
- Centraliser les logs
- Activer un WAF ou IDS

---

#### 📜 Licence

```markdown
© 2025 Virginie Lechene – Tous droits réservés
Reproduction interdite sans autorisation.
Usage pédagogique uniquement.







