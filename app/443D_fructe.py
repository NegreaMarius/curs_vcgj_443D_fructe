from flask import Flask

print ('443D_fructe')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>INformatii despre fructe 443D</h1>"
    return ret

@app.route("/capsuni", methods=['GET'])   
def get_capsuni():
    return "CAPSUNI"

app.run(host = "127.0.0.1", port = 5001)