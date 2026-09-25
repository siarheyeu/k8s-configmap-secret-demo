from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "app_name": "k8s-configmap-secret-demo",
        "environment": os.getenv("APP_ENV"),
        "version": os.getenv("APP_VERSION"),
        "color": os.getenv("APP_COLOR"),
        "secret_configured": bool(os.getenv("APP_TOKEN")),
        "hostname": socket.gethostname()
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
