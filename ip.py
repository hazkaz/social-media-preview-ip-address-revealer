from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_ip():
    ip = request.headers.get("x-forwarded-for")
    ip = ip.split(",")[-1] if ip else request.remote_addr
    return render_template('index.html', ip_address=ip)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
