from flask import Flask, render_template, jsonify
from database import get_recent_packets, get_alerts

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/packets")
def packets():
    data = get_recent_packets()
    return jsonify([{
        "id": r[0], "timestamp": r[1], "src_ip": r[2],
        "dst_ip": r[3], "protocol": r[4], "size": r[5]
    } for r in data])

@app.route("/api/alerts")
def alerts():
    data = get_alerts()
    return jsonify([{
        "id": r[0], "timestamp": r[1], "type": r[2],
        "src_ip": r[3], "detail": r[4]
    } for r in data])

if __name__ == "__main__":
    app.run(debug=True, port=5050)