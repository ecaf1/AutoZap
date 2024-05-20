import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print(" DATA: ", json.dumps(data, indent=4))
    return jsonify({"status": "Recebido com sucesso"}), 200
