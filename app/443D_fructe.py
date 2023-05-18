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
    
'''
 ------------------------------------
    #04. BELIŢOIU F.M. Rareş-Florian - mar
 ------------------------------------
'''

@app.route("/mar", methods=['GET'])
def obtine_mar():
    ret = "<h1>mar:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_mar()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_mar()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_mar()
    ret += "<br>"

    print("DBG: apel obtine_mar")
    return ret

@app.route("/mar/culoare", methods=['GET'])
def obtine_culoare_mar():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_mar()
    return ret

@app.route("/mar/gust", methods=['GET'])
def obtine_gust_mar():
    ret = ""
    ret += lib.biblioteca_fructe.gust_mar()
    return ret

@app.route("/mar/anotimp", methods=['GET'])
def obtine_anotimp_mar():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_mar()
    return ret
    
'''
 ------------------------------------
    #19. ŞPAN O. Lorin - vanata
 ------------------------------------
'''

@app.route("/vanata", methods=['GET'])
def obtine_vanata():
    ret = "<h1>vanata:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_vanata()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_vanata()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_vanata()
    ret += "<br>"

    print("DBG: apel obtine_vanata")
    return ret

@app.route("/vanata/culoare", methods=['GET'])
def obtine_culoare_vanata():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_vanata()
    return ret

@app.route("/vanata/gust", methods=['GET'])
def obtine_gust_vanata():
    ret = ""
    ret += lib.biblioteca_fructe.gust_vanata()
    return ret

@app.route("/vanata/anotimp", methods=['GET'])
def obtine_anotimp_vanata():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_vanata()
    return ret
 
'''
 ------------------------------------
    #25. VASILESCU P. Bogdan - piersica
 ------------------------------------
'''

@app.route("/piersica", methods=['GET'])
def obtine_piersica():
    ret = "<h1>piersica:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_piersica()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_piersica()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_piersica()
    ret += "<br>"

    print("DBG: apel obtine_piersica")
    return ret

@app.route("/piersica/culoare", methods=['GET'])
def obtine_culoare_piersica():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_piersica()
    return ret

@app.route("/piersica/gust", methods=['GET'])
def obtine_gust_piersica():
    ret = ""
    ret += lib.biblioteca_fructe.gust_piersica()
    return ret

@app.route("/piersica/anotimp", methods=['GET'])
def obtine_anotimp_piersica():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_piersica()
    return ret
    
    '''
 ------------------------------------
    #24. VASILE M. Vlad-Andrei - kiwi
 ------------------------------------
'''

@app.route("/kiwi", methods=['GET'])
def obtine_kiwi():
    ret = "<h1>kiwi:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_kiwi()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_kiwi()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_kiwi()
    ret += "<br>"

    print("DBG: apel obtine_kiwi")
    return ret

@app.route("/kiwi/culoare", methods=['GET'])
def obtine_culoare_kiwi():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_kiwi()
    return ret

@app.route("/kiwi/gust", methods=['GET'])
def obtine_gust_kiwi():
    ret = ""
    ret += lib.biblioteca_fructe.gust_kiwi()
    return ret

@app.route("/kiwi/anotimp", methods=['GET'])
def obtine_anotimp_kiwi():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_kiwi()
    return ret 
app.run(host = "127.0.0.1", port = 5002)
