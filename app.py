from flask import Flask, jsonify

app = Flask(__name__)

counter = 0  # STATE (sunucu tarafında tutuluyor)

@app.route("/")
def home():
    return "Stateful API çalışıyor - Barış Ocak"

@app.route("/stateful")
def stateful():
    global counter
    counter += 1
    return jsonify({
        "counter": counter,
        "owner": "Barış Ocak"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





