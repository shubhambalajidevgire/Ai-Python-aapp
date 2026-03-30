import sys
import os

# 🔥 Fix import path (VERY IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, jsonify

# Your AI controller
from app.controller import Controller

import subprocess
import tempfile

app = Flask(__name__)
ctrl = Controller()


# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# AI PROCESS ROUTE
# =========================
@app.route("/process", methods=["POST"])
def process():

    data = request.get_json(force=True)
    user_input = data.get("prompt") if data else ""

    result = ctrl.process_prompt(user_input)

    return jsonify(result)


# =========================
# RUN CODE ROUTE
# =========================
@app.route("/run", methods=["POST"])
def run_code():

    data = request.get_json(force=True)
    code = data.get("code") if data else None

    if not code:
        return jsonify({"output": "No code provided"})

    try:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
            f.write(code.encode())
            file_name = f.name

        # Execute code
        result = subprocess.run(
            ["python", file_name],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout if result.stdout else result.stderr

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"output": str(e)})


# =========================
# START SERVER
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
