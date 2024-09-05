from flask import Flask, jsonify, request;

app = Flask(__name__);

taches = [
    {"id": 1, "titre": "Apprendre Flask", "description": "Regarder un tutoriel Flask", "complete": False},
    {"id": 2, "titre": "Faire les courses", "description": "Acheter du lait et du pain", "complete": False},
]

@app.route('/')
def home():
    return "Mon API sur Flask"

# Récupérer les tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(taches)

# Récupérer une task spécifique
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id: int):
    task = next((tache for tache in taches if tache['id'] == id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({"Error": "Tache non trouvée"})

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)