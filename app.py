from flask import Flask, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

@app.route("/")
def home():
    return "Welcome to OS-Monitor API!"

@app.route("/stats")
def get_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    data = {
        "cpu": cpu_usage,
        "memory": {
            "total": memory_info.total,
            "used": memory_info.used,
            "percent": memory_info.percent
        },
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "percent": disk_usage.percent
        }
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
