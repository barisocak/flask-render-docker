from flask import Flask
import requests

app = Flask(__name__)

API_URL = "https://flask-render-docker.onrender.com/api/info"


@app.route("/")
def home():
    r = requests.get(API_URL)
    data = r.json()
    return f"""
    <h1>Mikro Hizmet Frontend</h1>
    <p>API Servis: {data['service']}</p>
    <p>Durum: {data['status']}</p>
    <p>Sahip: {data['owner']}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
