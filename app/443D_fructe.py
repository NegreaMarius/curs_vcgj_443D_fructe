from flask import Flask

import lib.biblioteca_fructe

print('443D_fructe')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre fructe (gr 443D)</h1>"
    return ret

'''
 ------------------------------------
 EXEMPLU START
 ------------------------------------
'''
@app.route("/afine", methods=['GET'])
def obtine_afine():
    ret = "<h1>Afine:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_afine()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_afine()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_afine()
    ret += "<br>"

    print("DBG: apel obtine_afine")

    return ret

@app.route("/afine/culoare", methods=['GET'])
def obtine_culoare_afine():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_afine()
    return ret

@app.route("/afine/gust", methods=['GET'])
def obtine_gust_afine():
    ret = ""
    ret += lib.biblioteca_fructe.gust_afine()
    return ret

@app.route("/afine/anotimp", methods=['GET'])
def obtine_anotimp_afine():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_afine()
    return ret

'''
 ------------------------------------
 ---------- EXEMPLU STOP ------------
 ------------------------------------
'''

app.run(host = "127.0.0.1", port = 5001)