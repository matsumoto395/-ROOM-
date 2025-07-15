# app/main.py
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Cloud Run が渡す PORT（デフォルト 8080）で待ち受け
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
