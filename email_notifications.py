#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module d'envoi d'emails pour la simulation Facebook
Permet d'envoyer des notifications par email aux utilisateurs
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ============================================
# CONFIGURATION EMAIL - À MODIFIER
# ============================================

# Votre adresse Gmail pour envoyer les emails
EMAIL_EXPEDITEUR = "fatimaelzahraadriouech@gmail.com"

# Votre mot de passe d'application Gmail (16 caractères)
MDPASSE_APP = "aney vzig dgby hfof"

# Serveur SMTP Gmail
SMTP_SERVEUR = "smtp.gmail.com"
SMTP_PORT = 587


# ============================================
# FONCTIONS D'ENVOI D'EMAILS
# ============================================

def envoyer_email(destinataire, sujet, message_html):
    """
    Fonction générique pour envoyer un email
    
    Args:
        destinataire (str): Email du destinataire
        sujet (str): Sujet de l'email
        message_html (str): Corps du message en HTML
    
    Returns:
        bool: True si envoyé avec succès, False sinon
    """
    try:
        # Créer le message
        msg = MIMEMultipart('alternative')
        msg['From'] = f"Facebook Simulation <{EMAIL_EXPEDITEUR}>"
        msg['To'] = destinataire
        msg['Subject'] = sujet
        
        # Ajouter le corps HTML
        partie_html = MIMEText(message_html, 'html', 'utf-8')
        msg.attach(partie_html)
        
        # Connexion au serveur SMTP
        serveur = smtplib.SMTP(SMTP_SERVEUR, SMTP_PORT)
        serveur.starttls()
        serveur.login(EMAIL_EXPEDITEUR, MDPASSE_APP.replace(" ", ""))
        
        # Envoi
        serveur.send_message(msg)
        serveur.quit()
        
        print(f"✓ Email envoyé à {destinataire}")
        return True
        
    except Exception as e:
        print(f"✗ Erreur envoi email: {str(e)}")
        return False


def email_bienvenue(nom_utilisateur, email_utilisateur):
    """
    Envoie un email de bienvenue lors de l'inscription
    """
    sujet = "Bienvenue sur Facebook !"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }}
            .container {{ background-color: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; }}
            .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ padding: 20px; color: #333; }}
            .footer {{ text-align: center; color: #65676b; font-size: 12px; margin-top: 20px; }}
            .button {{ background-color: #1877f2; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>facebook</h1>
            </div>
            <div class="content">
                <h2>Bienvenue {nom_utilisateur} !</h2>
                <p>Votre compte Facebook a été créé avec succès.</p>
                <p>Vous pouvez maintenant vous connecter et commencer à utiliser toutes les fonctionnalités :</p>
                <ul>
                    <li>Publier des statuts</li>
                    <li>Ajouter des amis</li>
                    <li>Partager des photos</li>
                    <li>Commenter et aimer les publications</li>
                </ul>
                <p style="text-align: center; margin-top: 30px;">
                    <a href="#" class="button">Se connecter maintenant</a>
                </p>
            </div>
            <div class="footer">
                <p>Ceci est une simulation Facebook - Projet éducatif</p>
                <p>Date d'inscription: {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)


def email_nouveau_ami(nom_utilisateur, email_utilisateur, nom_ami):
    """
    Notifie qu'une nouvelle demande d'ami a été reçue
    """
    sujet = f"{nom_ami} vous a envoyé une demande d'ami"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }}
            .container {{ background-color: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; }}
            .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; color: #333; }}
            .button {{ background-color: #42b72a; color: white; padding: 10px 20px; text-decoration: none; border-radius: 6px; margin: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>👥 Nouvelle demande d'ami</h2>
            </div>
            <div class="content">
                <p>Bonjour {nom_utilisateur},</p>
                <p><strong>{nom_ami}</strong> vous a envoyé une demande d'ami sur Facebook.</p>
                <p style="text-align: center; margin-top: 20px;">
                    <a href="#" class="button">Accepter</a>
                    <a href="#" class="button" style="background-color: #e4e6eb; color: #050505;">Refuser</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)


def email_nouveau_commentaire(nom_utilisateur, email_utilisateur, nom_auteur, texte_publication):
    """
    Notifie qu'un nouveau commentaire a été posté sur une publication
    """
    sujet = f"{nom_auteur} a commenté votre publication"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }}
            .container {{ background-color: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; }}
            .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; color: #333; }}
            .publication {{ background-color: #f0f2f5; padding: 15px; border-radius: 8px; margin: 15px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>💬 Nouveau commentaire</h2>
            </div>
            <div class="content">
                <p>Bonjour {nom_utilisateur},</p>
                <p><strong>{nom_auteur}</strong> a commenté votre publication :</p>
                <div class="publication">
                    <em>"{texte_publication[:100]}..."</em>
                </div>
                <p style="text-align: center; margin-top: 20px;">
                    <a href="#" style="background-color: #1877f2; color: white; padding: 10px 20px; text-decoration: none; border-radius: 6px;">Voir le commentaire</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)


def email_nouveau_like(nom_utilisateur, email_utilisateur, nom_auteur):
    """
    Notifie qu'une publication a reçu un like
    """
    sujet = f"{nom_auteur} a aimé votre publication"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }}
            .container {{ background-color: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; }}
            .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; color: #333; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>👍 Nouveau J'aime</h2>
            </div>
            <div class="content">
                <p style="font-size: 48px;">👍</p>
                <p>Bonjour {nom_utilisateur},</p>
                <p><strong>{nom_auteur}</strong> a aimé votre publication.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)


def email_recuperation_mdp(nom_utilisateur, email_utilisateur, code_verification):
    """
    Envoie un code de récupération de mot de passe
    """
    sujet = "Récupération de votre mot de passe Facebook"
    
    message = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; padding: 20px; }}
            .container {{ background-color: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; }}
            .header {{ background-color: #1877f2; color: white; padding: 20px; text-align: center; }}
            .content {{ padding: 20px; color: #333; }}
            .code {{ background-color: #e7f3ff; padding: 20px; text-align: center; font-size: 32px; font-weight: bold; letter-spacing: 5px; border-radius: 8px; margin: 20px 0; }}
            .warning {{ background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>🔐 Récupération de mot de passe</h2>
            </div>
            <div class="content">
                <p>Bonjour {nom_utilisateur},</p>
                <p>Vous avez demandé à réinitialiser votre mot de passe Facebook.</p>
                <p>Voici votre code de vérification :</p>
                <div class="code">{code_verification}</div>
                <div class="warning">
                    <strong>⚠️ Attention :</strong> Ne partagez jamais ce code avec qui que ce soit. Facebook ne vous demandera jamais votre code par email ou téléphone.
                </div>
                <p>Ce code expire dans 15 minutes.</p>
                <p>Si vous n'avez pas demandé cette récupération, ignorez cet email et votre mot de passe restera inchangé.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return envoyer_email(email_utilisateur, sujet, message)


# ============================================
# FONCTION DE TEST
# ============================================

def tester_email():
    """
    Fonction de test pour vérifier que l'envoi d'emails fonctionne
    """
    print("=" * 50)
    print("TEST DU SYSTÈME D'EMAILS - SIMULATION FACEBOOK")
    print("=" * 50)
    
    email_test = input("\nEntrez votre email pour le test: ")
    
    print("\n1. Test email de bienvenue...")
    email_bienvenue("TestUser", email_test)
    
    print("\n✓ Test terminé! Vérifiez votre boîte email.")


if __name__ == "__main__":
    tester_email()
