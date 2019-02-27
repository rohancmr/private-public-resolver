from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
	
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr, 'forwarder-for': request.headers['X-Forwarded-For']}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
