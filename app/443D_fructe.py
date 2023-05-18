from flask import Flask
import lib.biblioteca_fructe
app = Flask(__name__)
print('443D_fructe')

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>Informatii despre Fructe (Grupa 443D)</h1>"
    return ret

'''
 ------------------------------------
    #0. CRChende - Afine
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
    #10. NEGREA M. Marius-Ştefan - rodie
 ------------------------------------
'''

@app.route("/rodie", methods=['GET'])
def obtine_rodie():
    ret = "<h1>rodie:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_rodie()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_rodie()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_rodie()
    ret += "<br>"

    print("DBG: apel obtine_rodie")
    return ret

@app.route("/rodie/culoare", methods=['GET'])
def obtine_culoare_rodie():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_rodie()
    return ret

@app.route("/rodie/gust", methods=['GET'])
def obtine_gust_rodie():
    ret = ""
    ret += lib.biblioteca_fructe.gust_rodie()
    return ret

@app.route("/rodie/anotimp", methods=['GET'])
def obtine_anotimp_rodie():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_rodie()
    return ret

'''
 ------------------------------------
    #03. BĂNESCU A.F. Alexandru - capsuna
 ------------------------------------
'''

@app.route("/capsuna", methods=['GET'])
def obtine_capsuna():
    ret = "<h1>capsuna:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_capsuna()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_capsuna()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_capsuna()
    ret += "<br>"

    print("DBG: apel obtine_capsuna")
    return ret

@app.route("/capsuna/culoare", methods=['GET'])
def obtine_culoare_capsuna():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_capsuna()
    return ret

@app.route("/capsuna/gust", methods=['GET'])
def obtine_gust_capsuna():
    ret = ""
    ret += lib.biblioteca_fructe.gust_capsuna()
    return ret

@app.route("/capsuna/anotimp", methods=['GET'])
def obtine_anotimp_capsuna():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_capsuna()
    return ret
    
app.run(host = "127.0.0.1", port = 5002)
