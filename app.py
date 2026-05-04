from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:1b"

@app.route("/")
def index():
    return render_template("index.html", model=MODEL)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        }, timeout=300)   # 5 minutes

        result = response.json()
        reply = result["message"]["content"]
        return jsonify({"reply": reply})

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Ollama is not running. Start it with: ollama serve"}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": "Model timed out. Try a shorter message or restart Ollama."}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"Starting chat app with model: {MODEL}")
    print("Make sure Ollama is running: ollama serve")
    app.run(debug=True, port=5000)
