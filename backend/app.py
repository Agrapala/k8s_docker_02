from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify({
        "service": "backend",
        "status": "running",
        "env": os.getenv("ENV", "dev")
    })

@app.route("/health")
def health():
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
