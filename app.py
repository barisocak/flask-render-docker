from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/stateless")
def stateless():
    return jsonify({
        "message": "Stateless API çalışıyor",
        "owner": "Barış Ocak"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


