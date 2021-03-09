from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_ip():
    return render_template('index.html',ip_address=request.remote_addr)