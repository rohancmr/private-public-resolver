from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_my_ip():
    return request.headers['X-Forwarded-For'].split(':')[0], 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
