from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_ip():
    return render_template('index.html',ip_address=request.headers["x-forwarded-for"].split(",")[-1])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)