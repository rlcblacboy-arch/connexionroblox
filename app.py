from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def accueil():
    return "Serveur actif"

@app.route("/Mot de passe", methods=["POST"])
def identifiant():
    data = request.get_json() or {}
    print(data)
    pseudo = data.get("pwd", "")

    print("Mdp reçu :", pseudo)

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run()
