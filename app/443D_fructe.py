from flask import Flask

print('443D_fructe')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre fructe (gr 443D)</h1>"
    return ret


@app.route("/afine", methods=['GET'])
def get_afine():
    return "AFINE"

app.run(host = "127.0.0.1", port = 5001)