from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(pesan="Halo! Aplikasi ini berjalan di dalam Docker container")

@app.route("/tambah")
def tambah():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(a=a, b=b, hasil=a + b)

@app.route("/kali")
def kali():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(a=a, b=b, hasil=a * b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)