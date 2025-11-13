from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(status="ok", message="Secure CI Demo")

if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "8080"))
    app.run(host=host, port=port)