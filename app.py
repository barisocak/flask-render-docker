from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Microservice API çalışıyor - Barış Ocak"

@app.route("/api/info")
def info():
    return jsonify({
        "service": "Microservice API",
        "status": "active",
        "owner": "Barış Ocak"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

