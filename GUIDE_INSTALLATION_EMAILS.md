# 📧 GUIDE D'INSTALLATION - EMAILS POUR SIMULATION FACEBOOK

Ce guide vous explique comment ajouter l'envoi d'emails automatiques à votre projet de simulation Facebook.

---

## 📁 FICHIERS FOURNIS

1. **`email_notifications.py`** : Module d'envoi d'emails avec toutes les fonctions
2. **`exemple_integration.py`** : Exemples d'utilisation dans votre projet
3. **`GUIDE_INSTALLATION_EMAILS.md`** : Ce guide

---

## 🔧 ÉTAPE 1 : CONFIGURATION DE GMAIL

### 1.1 Activer l'authentification à deux facteurs

1. Allez sur https://myaccount.google.com/security
2. Activez la "Validation en deux étapes" si ce n'est pas déjà fait

### 1.2 Générer un mot de passe d'application

1. Allez sur https://myaccount.google.com/apppasswords
2. Connectez-vous à votre compte Gmail
3. Nom de l'application : tapez `Facebook Simulation`
4. Cliquez sur **"Créer"**
5. **COPIEZ LE CODE** affiché (format : `abcd efgh ijkl mnop`)
   - ⚠️ Il ne s'affichera qu'une seule fois !

---

## 📝 ÉTAPE 2 : CONFIGURATION DU FICHIER email_notifications.py

### 2.1 Ouvrir le fichier

```bash
notepad email_notifications.py
```

### 2.2 Modifier la configuration (lignes 15-18)

Trouvez ces lignes :

```python
# Votre adresse Gmail pour envoyer les emails
EMAIL_EXPEDITEUR = "votre.email@gmail.com"

# Votre mot de passe d'application Gmail (16 caractères)
MDPASSE_APP = "xxxx xxxx xxxx xxxx"
```

Remplacez par vos vraies informations :

```python
# Votre adresse Gmail pour envoyer les emails
EMAIL_EXPEDITEUR = "jean.dupont@gmail.com"  # ← VOTRE VRAI EMAIL

# Votre mot de passe d'application Gmail (16 caractères)
MDPASSE_APP = "abcd efgh ijkl mnop"  # ← VOTRE VRAI CODE
```

### 2.3 Sauvegarder

- **Ctrl + S** pour sauvegarder
- Fermez l'éditeur

---

## ✅ ÉTAPE 3 : TESTER LE SYSTÈME

### 3.1 Lancer le test

```bash
python email_notifications.py
```

### 3.2 Entrer votre email

```
TEST DU SYSTÈME D'EMAILS - SIMULATION FACEBOOK
==================================================

Entrez votre email pour le test: votre.email@gmail.com
```

### 3.3 Résultat attendu

```
1. Test email de bienvenue...
✓ Email envoyé à votre.email@gmail.com

✓ Test terminé! Vérifiez votre boîte email.
```

### 3.4 Vérifier votre boîte email

Vous devriez recevoir un email de bienvenue avec le design Facebook ! 🎉

---

## 🔌 ÉTAPE 4 : INTÉGRATION DANS VOTRE PROJET

### 4.1 Structure de projet recommandée

```
votre_projet_facebook/
│
├── simulation_facebook.py      # Votre fichier principal
├── email_notifications.py      # Module d'emails (nouveau)
├── exemple_integration.py      # Exemples (référence)
└── ... vos autres fichiers ...
```

### 4.2 Importer le module dans votre fichier principal

Au début de votre fichier `simulation_facebook.py`, ajoutez :

```python
# Importer les fonctions d'email
from email_notifications import (
    email_bienvenue,
    email_nouveau_ami,
    email_nouveau_commentaire,
    email_nouveau_like,
    email_recuperation_mdp
)
```

---

## 📧 ÉTAPE 5 : UTILISATION DANS VOTRE CODE

### Exemple 1 : Email de bienvenue lors de l'inscription

```python
def inscription():
    # Votre code d'inscription existant...
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    email = input("Email: ")
    mdp = input("Mot de passe: ")
    
    # Créer le compte dans votre base de données
    # ... votre code ...
    
    # 🆕 ENVOYER L'EMAIL DE BIENVENUE
    nom_complet = f"{prenom} {nom}"
    email_bienvenue(nom_complet, email)
    
    print("✓ Compte créé! Email de bienvenue envoyé.")
```

### Exemple 2 : Notification de demande d'ami

```python
def envoyer_demande_ami(expediteur, destinataire):
    # Votre code pour enregistrer la demande...
    # ... votre code ...
    
    # 🆕 NOTIFIER PAR EMAIL
    email_nouveau_ami(
        destinataire['nom'],      # Nom du destinataire
        destinataire['email'],    # Email du destinataire
        expediteur['nom']         # Nom de l'expéditeur
    )
    
    print(f"✓ Demande envoyée à {destinataire['nom']}")
```

### Exemple 3 : Notification de nouveau commentaire

```python
def ajouter_commentaire(publication, auteur_commentaire, texte):
    # Votre code pour enregistrer le commentaire...
    # ... votre code ...
    
    # 🆕 NOTIFIER L'AUTEUR DE LA PUBLICATION
    email_nouveau_commentaire(
        publication['auteur']['nom'],      # Nom de l'auteur
        publication['auteur']['email'],    # Email de l'auteur
        auteur_commentaire['nom'],         # Nom du commentateur
        publication['texte']               # Texte de la publication
    )
    
    print("✓ Commentaire ajouté et auteur notifié")
```

### Exemple 4 : Notification de like

```python
def liker_publication(publication, utilisateur):
    # Votre code pour enregistrer le like...
    # ... votre code ...
    
    # 🆕 NOTIFIER L'AUTEUR
    email_nouveau_like(
        publication['auteur']['nom'],
        publication['auteur']['email'],
        utilisateur['nom']
    )
    
    print("✓ Like enregistré!")
```

### Exemple 5 : Récupération de mot de passe

```python
def mot_de_passe_oublie(email_utilisateur):
    import random
    
    # Rechercher l'utilisateur
    utilisateur = chercher_utilisateur_par_email(email_utilisateur)
    
    if not utilisateur:
        print("❌ Email non trouvé")
        return
    
    # Générer un code aléatoire
    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    # Sauvegarder le code (votre logique...)
    # ... votre code ...
    
    # 🆕 ENVOYER LE CODE PAR EMAIL
    email_recuperation_mdp(
        utilisateur['nom'],
        email_utilisateur,
        code
    )
    
    print(f"✓ Code {code} envoyé par email")
    return code
```

---

## 🎮 ÉTAPE 6 : TESTER AVEC LE MENU INTERACTIF

Le fichier `exemple_integration.py` contient un menu de démonstration.

### Lancer le menu

```bash
python exemple_integration.py
```

### Menu interactif

```
============================================================
DÉMONSTRATION - EMAILS DANS SIMULATION FACEBOOK
============================================================

📧 Entrez votre email pour les tests: votre.email@gmail.com

------------------------------------------------------------
Que voulez-vous tester ?
------------------------------------------------------------
1. Email de bienvenue (inscription)
2. Notification de demande d'ami
3. Notification de nouveau commentaire
4. Notification de nouveau like
5. Récupération de mot de passe
0. Quitter
------------------------------------------------------------

Votre choix: 
```

Testez chaque type d'email pour voir le résultat !

---

## 🎨 TYPES D'EMAILS DISPONIBLES

| Fonction | Quand l'utiliser | Paramètres |
|----------|------------------|------------|
| `email_bienvenue()` | Inscription d'un nouvel utilisateur | nom, email |
| `email_nouveau_ami()` | Demande d'ami envoyée | nom_destinataire, email_destinataire, nom_expediteur |
| `email_nouveau_commentaire()` | Quelqu'un commente une publication | nom_auteur, email_auteur, nom_commentateur, texte_pub |
| `email_nouveau_like()` | Quelqu'un like une publication | nom_auteur, email_auteur, nom_liker |
| `email_recuperation_mdp()` | Mot de passe oublié | nom, email, code_verification |

---

## ❌ DÉPANNAGE

### Erreur : "Authentification échouée"

**Solution :**
1. Vérifiez que vous avez bien utilisé un **mot de passe d'application** (pas votre mot de passe Gmail normal)
2. Vérifiez que le code est correct (16 caractères)
3. Régénérez un nouveau mot de passe d'application

### Les emails n'arrivent pas

**Vérifiez :**
1. La boîte **spam/courrier indésirable**
2. Que l'adresse email est correcte
3. Votre connexion internet

### Erreur : "Module not found"

**Solution :**
```bash
pip install --upgrade setuptools
```

Les modules `smtplib` et `email` sont inclus dans Python par défaut.

---

## 🔒 SÉCURITÉ

### ⚠️ IMPORTANT

- ✅ Ne partagez JAMAIS votre mot de passe d'application
- ✅ Ne publiez JAMAIS le fichier `email_notifications.py` avec vos mots de passe sur internet
- ✅ Gardez vos identifiants en sécurité
- ✅ Utilisez `.gitignore` si vous utilisez Git :

```
# Dans .gitignore
email_notifications.py
```

### Alternative sécurisée : Variables d'environnement

Pour plus de sécurité, vous pouvez utiliser des variables d'environnement :

```python
import os

EMAIL_EXPEDITEUR = os.environ.get('FB_EMAIL')
MDPASSE_APP = os.environ.get('FB_PASSWORD')
```

---

## 📊 RÉCAPITULATIF

### ✅ Checklist d'installation

- [ ] Mot de passe d'application Gmail généré
- [ ] Fichier `email_notifications.py` configuré avec vos identifiants
- [ ] Test du système réussi (`python email_notifications.py`)
- [ ] Module importé dans votre projet principal
- [ ] Au moins un type d'email testé dans votre simulation

---

## 🚀 ALLER PLUS LOIN

### Personnaliser les emails

Vous pouvez modifier les templates HTML dans `email_notifications.py` :
- Changer les couleurs
- Ajouter votre logo
- Modifier le texte
- Ajouter des boutons

### Ajouter de nouveaux types d'emails

Créez de nouvelles fonctions dans `email_notifications.py` :
- Email de confirmation de compte
- Email d'anniversaire
- Email de résumé hebdomadaire
- Email de nouveau message privé

### Exemple de nouvelle fonction

```python
def email_anniversaire(nom_utilisateur, email_utilisateur):
    sujet = f"Joyeux anniversaire {nom_utilisateur} ! 🎉"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <!-- Votre template HTML ici -->
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)
```

---

## 💡 CONSEILS

1. **Testez d'abord** avec votre propre email avant d'envoyer à d'autres
2. **N'envoyez pas trop d'emails** pour éviter d'être marqué comme spam
3. **Respectez la vie privée** des utilisateurs de votre simulation
4. **Ajoutez une option** pour désactiver les notifications par email

---

**Bon développement ! 🚀**

En cas de problème, relisez attentivement chaque étape de ce guide.
