#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXEMPLE D'INTÉGRATION DES EMAILS DANS VOTRE SIMULATION FACEBOOK

Ce fichier montre comment utiliser le module email_notifications.py
dans votre projet de simulation Facebook existant.
"""

# Importer le module d'emails
from email_notifications import (
    email_bienvenue,
    email_nouveau_ami,
    email_nouveau_commentaire,
    email_nouveau_like,
    email_recuperation_mdp
)

# ============================================
# EXEMPLE 1: LORS DE L'INSCRIPTION
# ============================================

def creer_compte_utilisateur(nom, prenom, email, mdp):
    """
    Exemple de fonction d'inscription avec envoi d'email
    """
    print(f"Création du compte pour {nom} {prenom}...")
    
    # Créer le compte dans votre base de données
    # ... votre code ici ...
    
    # Envoyer l'email de bienvenue
    nom_complet = f"{prenom} {nom}"
    email_bienvenue(nom_complet, email)
    
    print("✓ Compte créé et email de bienvenue envoyé!")


# ============================================
# EXEMPLE 2: DEMANDE D'AMI
# ============================================

def envoyer_demande_ami(utilisateur_expediteur, utilisateur_destinataire):
    """
    Exemple de fonction pour envoyer une demande d'ami
    """
    print(f"{utilisateur_expediteur['nom']} envoie une demande à {utilisateur_destinataire['nom']}")
    
    # Enregistrer la demande dans votre base de données
    # ... votre code ici ...
    
    # Envoyer la notification par email
    email_nouveau_ami(
        utilisateur_destinataire['nom'],
        utilisateur_destinataire['email'],
        utilisateur_expediteur['nom']
    )
    
    print("✓ Demande envoyée et notification par email!")


# ============================================
# EXEMPLE 3: NOUVEAU COMMENTAIRE
# ============================================

def ajouter_commentaire(publication, auteur_commentaire, texte_commentaire):
    """
    Exemple de fonction pour ajouter un commentaire
    """
    print(f"{auteur_commentaire['nom']} commente la publication...")
    
    # Enregistrer le commentaire
    # ... votre code ici ...
    
    # Notifier l'auteur de la publication par email
    email_nouveau_commentaire(
        publication['auteur']['nom'],
        publication['auteur']['email'],
        auteur_commentaire['nom'],
        publication['texte']
    )
    
    print("✓ Commentaire ajouté et auteur notifié!")


# ============================================
# EXEMPLE 4: NOUVEAU LIKE
# ============================================

def aimer_publication(publication, utilisateur):
    """
    Exemple de fonction pour liker une publication
    """
    print(f"{utilisateur['nom']} aime la publication...")
    
    # Enregistrer le like
    # ... votre code ici ...
    
    # Notifier l'auteur par email
    email_nouveau_like(
        publication['auteur']['nom'],
        publication['auteur']['email'],
        utilisateur['nom']
    )
    
    print("✓ Like enregistré et auteur notifié!")


# ============================================
# EXEMPLE 5: RÉCUPÉRATION DE MOT DE PASSE
# ============================================

def mot_de_passe_oublie(email_utilisateur):
    """
    Exemple de fonction pour la récupération de mot de passe
    """
    import random
    
    print(f"Demande de récupération pour {email_utilisateur}...")
    
    # Rechercher l'utilisateur dans la base de données
    # ... votre code ici ...
    # utilisateur = chercher_utilisateur_par_email(email_utilisateur)
    
    # Simuler un utilisateur
    utilisateur = {"nom": "Jean Dupont", "email": email_utilisateur}
    
    # Générer un code de vérification aléatoire
    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    # Sauvegarder le code dans la base de données
    # ... votre code ici ...
    
    # Envoyer l'email avec le code
    email_recuperation_mdp(utilisateur['nom'], email_utilisateur, code)
    
    print(f"✓ Code {code} envoyé par email!")
    return code


# ============================================
# EXEMPLE COMPLET: MENU DE DÉMONSTRATION
# ============================================

def menu_demonstration():
    """
    Menu interactif pour tester les différentes fonctionnalités
    """
    print("\n" + "=" * 60)
    print("DÉMONSTRATION - EMAILS DANS SIMULATION FACEBOOK")
    print("=" * 60)
    
    email_test = input("\n📧 Entrez votre email pour les tests: ")
    
    while True:
        print("\n" + "-" * 60)
        print("Que voulez-vous tester ?")
        print("-" * 60)
        print("1. Email de bienvenue (inscription)")
        print("2. Notification de demande d'ami")
        print("3. Notification de nouveau commentaire")
        print("4. Notification de nouveau like")
        print("5. Récupération de mot de passe")
        print("0. Quitter")
        print("-" * 60)
        
        choix = input("\nVotre choix: ")
        
        if choix == "1":
            nom = input("Nom de l'utilisateur: ")
            email_bienvenue(nom, email_test)
            print("✓ Email de bienvenue envoyé!")
            
        elif choix == "2":
            nom_ami = input("Nom de l'ami: ")
            email_nouveau_ami("Vous", email_test, nom_ami)
            print("✓ Notification d'ami envoyée!")
            
        elif choix == "3":
            nom_commentateur = input("Nom du commentateur: ")
            email_nouveau_commentaire("Vous", email_test, nom_commentateur, 
                                     "Quelle belle journée aujourd'hui!")
            print("✓ Notification de commentaire envoyée!")
            
        elif choix == "4":
            nom_liker = input("Nom de la personne qui like: ")
            email_nouveau_like("Vous", email_test, nom_liker)
            print("✓ Notification de like envoyée!")
            
        elif choix == "5":
            code = mot_de_passe_oublie(email_test)
            print(f"✓ Code de récupération envoyé: {code}")
            
        elif choix == "0":
            print("\n👋 Au revoir!")
            break
            
        else:
            print("❌ Choix invalide!")
        
        input("\nAppuyez sur Entrée pour continuer...")


# ============================================
# EXEMPLES D'INTÉGRATION DANS VOTRE CODE
# ============================================

"""
DANS VOTRE FICHIER PRINCIPAL (simulation_facebook.py):

# Au début du fichier, importer le module
from email_notifications import (
    email_bienvenue, 
    email_nouveau_ami,
    email_nouveau_commentaire,
    email_nouveau_like,
    email_recuperation_mdp
)

# Dans votre fonction d'inscription
def inscription():
    # ... votre code existant ...
    
    # Après avoir créé le compte, envoyer l'email
    email_bienvenue(nom_utilisateur, email_utilisateur)

# Dans votre fonction pour ajouter un ami
def ajouter_ami():
    # ... votre code existant ...
    
    # Après avoir envoyé la demande
    email_nouveau_ami(destinataire['nom'], destinataire['email'], expediteur['nom'])

# Dans votre fonction pour commenter
def commenter():
    # ... votre code existant ...
    
    # Après avoir ajouté le commentaire
    email_nouveau_commentaire(auteur_pub['nom'], auteur_pub['email'], 
                             commentateur['nom'], publication['texte'])

# Dans votre fonction pour liker
def liker():
    # ... votre code existant ...
    
    # Après avoir enregistré le like
    email_nouveau_like(auteur_pub['nom'], auteur_pub['email'], liker['nom'])
"""


if __name__ == "__main__":
    menu_demonstration()
