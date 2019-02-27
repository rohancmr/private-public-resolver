from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
	
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return request.headers['X-Forwarded-For'].split(':')[0], 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
