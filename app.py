from flask import Flask

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def home():
    return "Bienvenue sur ma première application Flask !"

# Route qui dit bonjour à l'utilisateur
@app.route('/salut/<nom>')
def salut(nom):
    return f"Salut, {nom} ! Bienvenue sur Flask."

# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
