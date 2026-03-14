# ============================================================
#   PROJET : Détection d'URL de Phishing
#   Étapes 3 → 6 : Chargement, Split, Entraînement, Évaluation
# ============================================================

# ── ÉTAPE 0 : Installer les librairies (à faire une seule fois)
# Ouvre ton terminal et tape :
# pip install pandas scikit-learn matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             classification_report, confusion_matrix)

# ============================================================
# ÉTAPE 3 : Charger le dataset UCI Phishing Websites
# ============================================================
print("=" * 50)
print("ÉTAPE 3 : Chargement du dataset")
print("=" * 50)

# ⚠️ Mets le bon nom de ton fichier CSV ici
df = pd.read_csv("data/donnees_collectees.csv")


print(f"✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
print("\nAperçu des données :")
print(df.head())
print("\nDistribution des classes :")
print(df['class'].value_counts())
# Dans le dataset UCI :  1 = Légitime  |  -1 = Phishing

# ============================================================
# ÉTAPE 4 : Séparer les données (Train / Test)
# ============================================================
print("\n" + "=" * 50)
print("ÉTAPE 4 : Séparation Train / Test")
print("=" * 50)

X = df.drop('class', axis=1)   # Features (toutes les colonnes sauf Result)
y = df['class']                 # Labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% pour le test
    random_state=42      # reproductibilité
)

print(f"✅ Données d'entraînement : {X_train.shape[0]} exemples")
print(f"✅ Données de test        : {X_test.shape[0]} exemples")

# ============================================================
# ÉTAPE 5 : Entraîner le modèle Random Forest
# ============================================================
print("\n" + "=" * 50)
print("ÉTAPE 5 : Entraînement Random Forest")
print("=" * 50)

model = RandomForestClassifier(
    n_estimators=100,   # 100 arbres de décision
    random_state=42
)

print("⏳ Entraînement en cours...")
model.fit(X_train, y_train)
print("✅ Modèle entraîné avec succès !")

# ============================================================
# ÉTAPE 6 : Évaluation du modèle
# ============================================================
print("\n" + "=" * 50)
print("ÉTAPE 6 : Évaluation du modèle")
print("=" * 50)

y_pred = model.predict(X_test)

accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=-1)
recall    = recall_score(y_test, y_pred, pos_label=-1)
f1        = f1_score(y_test, y_pred, pos_label=-1)

print(f"\n📊 RÉSULTATS :")
print(f"   Accuracy  : {accuracy  * 100:.2f}%")
print(f"   Precision : {precision * 100:.2f}%")
print(f"   Recall    : {recall    * 100:.2f}%")
print(f"   F1-Score  : {f1        * 100:.2f}%")

print("\n📋 Rapport complet :")
print(classification_report(y_test, y_pred,
      target_names=["Phishing (-1)", "Légitime (1)"]))

# ============================================================
# ÉTAPE 7 : Visualisations
# ============================================================

# -- Matrice de confusion --
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Phishing", "Légitime"],
            yticklabels=["Phishing", "Légitime"])
plt.title("Matrice de Confusion")
plt.ylabel("Réel")
plt.xlabel("Prédit")
plt.tight_layout()
import os
os.makedirs("data", exist_ok=True)
plt.savefig("data/matrice_confusion.png")
plt.show()
print("✅ Matrice de confusion sauvegardée")

# -- Importance des features --
importances = pd.Series(model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 6))
importances.plot(kind='bar', color='#1877f2')
plt.title("Top 15 Features les plus importantes")
plt.ylabel("Importance")
plt.xlabel("Feature")
plt.tight_layout()
plt.savefig("data/feature_importance.png")
plt.show()
print("✅ Graphique feature importance sauvegardé")

print("\n🎉 PROJET TERMINÉ !")
