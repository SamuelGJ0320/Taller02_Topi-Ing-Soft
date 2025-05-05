from flask import Flask, jsonify, render_template_string
import json
import random
import socket
from pathlib import Path

app = Flask(__name__)

def get_pokeneas_data():
    json_path = Path(__file__).parent / "pokeneas.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

pokeneas = get_pokeneas_data()
container_id = socket.gethostname()  # ID del contenedor

@app.route("/api/pokenea")
def api_pokenea():
    p = random.choice(pokeneas)
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "contenedor_id": container_id
    })

@app.route("/pokenea")
def show_pokenea():
    p = random.choice(pokeneas)
    html = f"""
    <h1>{p['nombre']}</h1>
    <img src="{p['imagen']}" alt="{p['nombre']}" width="300">
    <p><strong>Frase:</strong> {p['frase']}</p>
    <p><strong>Contenedor ID:</strong> {container_id}</p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
