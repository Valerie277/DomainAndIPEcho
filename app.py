
from flask import Flask;
from flask import request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", Domain=request.headers['Host'])
    # return "The Domain {} is not available".format(request.headers['Host'])


@app.route("/ip4", methods=["GET"])
def get_my_ip_v4():
    return "Deine IPv4 Adresse ist: {}".format(request.remote_addr)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')