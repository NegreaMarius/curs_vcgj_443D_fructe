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
    
    '''
 ------------------------------------
    #22. TUDOSE V.D. Bogdan-Mihai - portocala
 ------------------------------------
'''

@app.route("/portocala", methods=['GET'])
def obtine_portocala():
    ret = "<h1>portocala:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_portocala()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_portocala()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_portocala()
    ret += "<br>"

    print("DBG: apel obtine_portocala")
    return ret

@app.route("/portocala/culoare", methods=['GET'])
def obtine_culoare_portocala():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_portocala()
    return ret

@app.route("/portocala/gust", methods=['GET'])
def obtine_gust_portocala():
    ret = ""
    ret += lib.biblioteca_fructe.gust_portocala()
    return ret

@app.route("/portocala/anotimp", methods=['GET'])
def obtine_anotimp_portocala():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_portocala()
    return ret

'''
 ------------------------------------
    #17. STĂNCULESCU M. Andrei - avocado
 ------------------------------------
'''

@app.route("/avocado", methods=['GET'])
def obtine_avocado():
    ret = "<h1>avocado:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_avocado()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_avocado()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_avocado()
    ret += "<br>"

    print("DBG: apel obtine_avocado")
    return ret

@app.route("/avocado/culoare", methods=['GET'])
def obtine_culoare_avocado():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_avocado()
    return ret

@app.route("/avocado/gust", methods=['GET'])
def obtine_gust_avocado():
    ret = ""
    ret += lib.biblioteca_fructe.gust_avocado()
    return ret

@app.route("/avocado/anotimp", methods=['GET'])
def obtine_anotimp_avocado():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_avocado()
    return ret

'''
 ------------------------------------
    #23. URZICĂ C. Andrei-Octavian - ananas
 ------------------------------------
'''

@app.route("/ananas", methods=['GET'])
def obtine_ananas():
    ret = "<h1>ananas:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_ananas()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_ananas()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_ananas()
    ret += "<br>"

    print("DBG: apel obtine_ananas")
    return ret

@app.route("/ananas/culoare", methods=['GET'])
def obtine_culoare_ananas():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_ananas()
    return ret

@app.route("/ananas/gust", methods=['GET'])
def obtine_gust_ananas():
    ret = ""
    ret += lib.biblioteca_fructe.gust_ananas()
    return ret

@app.route("/ananas/anotimp", methods=['GET'])
def obtine_anotimp_ananas():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_ananas()
    return ret
    
    '''
 ------------------------------------
    #11. PARPALEA I.V. Alexandra - pepene_galben
 ------------------------------------
'''

@app.route("/pepene_galben", methods=['GET'])
def obtine_pepene_galben():
    ret = "<h1>pepene_galben:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_pepene_galben()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_pepene_galben()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_pepene_galben()
    ret += "<br>"

    print("DBG: apel obtine_pepene_galben")
    return ret

@app.route("/pepene_galben/culoare", methods=['GET'])
def obtine_culoare_pepene_galben():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_pepene_galben()
    return ret

@app.route("/pepene_galben/gust", methods=['GET'])
def obtine_gust_pepene_galben():
    ret = ""
    ret += lib.biblioteca_fructe.gust_pepene_galben()
    return ret

@app.route("/pepene_galben/anotimp", methods=['GET'])
def obtine_anotimp_pepene_galben():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_pepene_galben()
    return ret
    
    '''
 ------------------------------------
    #14. ROŞU E. Georgiana - pepene_rosu
 ------------------------------------
'''

@app.route("/pepene_rosu", methods=['GET'])
def obtine_pepene_rosu():
    ret = "<h1>pepene_rosu:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_pepene_rosu()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_pepene_rosu()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_pepene_rosu()
    ret += "<br>"

    print("DBG: apel obtine_pepene_rosu")
    return ret

@app.route("/pepene_rosu/culoare", methods=['GET'])
def obtine_culoare_pepene_rosu():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_pepene_rosu()
    return ret

@app.route("/pepene_rosu/gust", methods=['GET'])
def obtine_gust_pepene_rosu():
    ret = ""
    ret += lib.biblioteca_fructe.gust_pepene_rosu()
    return ret

@app.route("/pepene_rosu/anotimp", methods=['GET'])
def obtine_anotimp_pepene_rosu():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_pepene_rosu()
    return ret

'''
 ------------------------------------
    #02. ARNĂUTU V. Gabriel-Dorin - clementina
 ------------------------------------
'''

@app.route("/clementina", methods=['GET'])
def obtine_clementina():
    ret = "<h1>clementina:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_clementina()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_clementina()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_clementina()
    ret += "<br>"

    print("DBG: apel obtine_clementina")
    return ret

@app.route("/clementina/culoare", methods=['GET'])
def obtine_culoare_clementina():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_clementina()
    return ret

@app.route("/clementina/gust", methods=['GET'])
def obtine_gust_clementina():
    ret = ""
    ret += lib.biblioteca_fructe.gust_clementina()
    return ret

@app.route("/clementina/anotimp", methods=['GET'])
def obtine_anotimp_clementina():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_clementina()
    return ret
    
'''
 ------------------------------------
    #21. TEODORESCU T.I. Ciprian - banana
 ------------------------------------
'''

@app.route("/banana", methods=['GET'])
def obtine_banana():
    ret = "<h1>banana:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_banana()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_banana()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_banana()
    ret += "<br>"

    print("DBG: apel obtine_banana")
    return ret

@app.route("/banana/culoare", methods=['GET'])
def obtine_culoare_banana():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_banana()
    return ret

@app.route("/banana/gust", methods=['GET'])
def obtine_gust_banana():
    ret = ""
    ret += lib.biblioteca_fructe.gust_banana()
    return ret

@app.route("/banana/anotimp", methods=['GET'])
def obtine_anotimp_banana():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_banana()
    return ret

'''
 ------------------------------------
    #20. ŞTEFAN E. Ion-Alexandru - strugure
 ------------------------------------
'''

@app.route("/strugure", methods=['GET'])
def obtine_strugure():
    ret = "<h1>strugure:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_strugure()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_strugure()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_strugure()
    ret += "<br>"

    print("DBG: apel obtine_strugure")
    return ret

@app.route("/strugure/culoare", methods=['GET'])
def obtine_culoare_strugure():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_strugure()
    return ret

@app.route("/strugure/gust", methods=['GET'])
def obtine_gust_strugure():
    ret = ""
    ret += lib.biblioteca_fructe.gust_strugure()
    return ret

@app.route("/strugure/anotimp", methods=['GET'])
def obtine_anotimp_strugure():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_strugure()
    return ret

'''
 ------------------------------------
    #13. RODRIGUEZ-RAMIREZ-ZAHARIA J.A. Nicolas - mandarina
 ------------------------------------
'''

@app.route("/mandarina", methods=['GET'])
def obtine_mandarina():
    ret = "<h1>mandarina:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_mandarina()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_mandarina()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_mandarina()
    ret += "<br>"

    print("DBG: apel obtine_mandarina")
    return ret

@app.route("/mandarina/culoare", methods=['GET'])
def obtine_culoare_mandarina():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_mandarina()
    return ret

@app.route("/mandarina/gust", methods=['GET'])
def obtine_gust_mandarina():
    ret = ""
    ret += lib.biblioteca_fructe.gust_mandarina()
    return ret

@app.route("/mandarina/anotimp", methods=['GET'])
def obtine_anotimp_mandarina():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_mandarina()
    return ret

'''
 ------------------------------------
    #18. ŞERBULEA J. Ana-Corina - curmala
 ------------------------------------
'''

@app.route("/curmala", methods=['GET'])
def obtine_curmala():
    ret = "<h1>curmala:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_curmala()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_curmala()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_curmala()
    ret += "<br>"

    print("DBG: apel obtine_curmala")
    return ret

@app.route("/curmala/culoare", methods=['GET'])
def obtine_culoare_curmala():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_curmala()
    return ret

@app.route("/curmala/gust", methods=['GET'])
def obtine_gust_curmala():
    ret = ""
    ret += lib.biblioteca_fructe.gust_curmala()
    return ret

@app.route("/curmala/anotimp", methods=['GET'])
def obtine_anotimp_curmala():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_curmala()
    return ret
    
'''
 ------------------------------------
    #05. GHIOJDEANU C.O. Ştefan-Mihnea - cireasa
 ------------------------------------
'''

@app.route("/cireasa", methods=['GET'])
def obtine_cireasa():
    ret = "<h1>cireasa:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_cireasa()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_cireasa()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_cireasa()
    ret += "<br>"

    print("DBG: apel obtine_cireasa")
    return ret

@app.route("/cireasa/culoare", methods=['GET'])
def obtine_culoare_cireasa():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_cireasa()
    return ret

@app.route("/cireasa/gust", methods=['GET'])
def obtine_gust_cireasa():
    ret = ""
    ret += lib.biblioteca_fructe.gust_cireasa()
    return ret

@app.route("/cireasa/anotimp", methods=['GET'])
def obtine_anotimp_cireasa():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_cireasa()
    return ret
    
    
'''
 ------------------------------------
    #16. SIMA D. Andrei-Mihai - papaya
 ------------------------------------
'''

@app.route("/papaya", methods=['GET'])
def obtine_papaya():
    ret = "<h1>papaya:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_papaya()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_papaya()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_papaya()
    ret += "<br>"

    print("DBG: apel obtine_papaya")
    return ret

@app.route("/papaya/culoare", methods=['GET'])
def obtine_culoare_papaya():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_papaya()
    return ret

@app.route("/papaya/gust", methods=['GET'])
def obtine_gust_papaya():
    ret = ""
    ret += lib.biblioteca_fructe.gust_papaya()
    return ret

@app.route("/papaya/anotimp", methods=['GET'])
def obtine_anotimp_papaya():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_papaya()
    return ret
    
'''
 ------------------------------------
    #06. IANCU M. Matei-Theodor - smochina
 ------------------------------------
'''

@app.route("/smochina", methods=['GET'])
def obtine_smochina():
    ret = "<h1>smochina:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_smochina()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_smochina()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_smochina()
    ret += "<br>"

    print("DBG: apel obtine_smochina")
    return ret

@app.route("/smochina/culoare", methods=['GET'])
def obtine_culoare_smochina():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_smochina()
    return ret

@app.route("/smochina/gust", methods=['GET'])
def obtine_gust_smochina():
    ret = ""
    ret += lib.biblioteca_fructe.gust_smochina()
    return ret

@app.route("/smochina/anotimp", methods=['GET'])
def obtine_anotimp_smochina():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_smochina()
    return ret

'''
 ------------------------------------
    #12. ROCEANU E. Adelin-Adrian - caisa
 ------------------------------------
'''

@app.route("/caisa", methods=['GET'])
def obtine_caisa():
    ret = "<h1>caisa:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_caisa()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_caisa()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_caisa()
    ret += "<br>"

    print("DBG: apel obtine_caisa")
    return ret

@app.route("/caisa/culoare", methods=['GET'])
def obtine_culoare_caisa():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_caisa()
    return ret

@app.route("/caisa/gust", methods=['GET'])
def obtine_gust_caisa():
    ret = ""
    ret += lib.biblioteca_fructe.gust_caisa()
    return ret

@app.route("/caisa/anotimp", methods=['GET'])
def obtine_anotimp_caisa():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_caisa()
    return ret

'''
 ------------------------------------
    #08. LABEŞ N.G. Andreea-Georgiana - pruna
 ------------------------------------
'''

@app.route("/pruna", methods=['GET'])
def obtine_pruna():
    ret = "<h1>pruna:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_pruna()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_pruna()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_pruna()
    ret += "<br>"

    print("DBG: apel obtine_pruna")
    return ret

@app.route("/pruna/culoare", methods=['GET'])
def obtine_culoare_pruna():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_pruna()
    return ret

@app.route("/pruna/gust", methods=['GET'])
def obtine_gust_pruna():
    ret = ""
    ret += lib.biblioteca_fructe.gust_pruna()
    return ret

@app.route("/pruna/anotimp", methods=['GET'])
def obtine_anotimp_pruna():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_pruna()
    return ret
    
'''
 ------------------------------------
    #01. ALBU O.T. Marius-Andrei - visine
 ------------------------------------
'''

@app.route("/visine", methods=['GET'])
def obtine_visine():
    ret = "<h1>visine:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_visine()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_visine()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_visine()
    ret += "<br>"

    print("DBG: apel obtine_visine")
    return ret

@app.route("/visine/culoare", methods=['GET'])
def obtine_culoare_visine():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_visine()
    return ret

@app.route("/visine/gust", methods=['GET'])
def obtine_gust_visine():
    ret = ""
    ret += lib.biblioteca_fructe.gust_visine()
    return ret

@app.route("/visine/anotimp", methods=['GET'])
def obtine_anotimp_visine():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_visine()
    return ret
    
'''
 ------------------------------------
    #15. RUŢĂ M. Tiberiu-Mirel - mango
 ------------------------------------
'''

@app.route("/mango", methods=['GET'])
def obtine_mango():
    ret = "<h1>mango:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_fructe.culoare_mango()
    ret += "<br>"

    ret += "<b>Gust: </b>"
    ret += lib.biblioteca_fructe.gust_mango()
    ret += "<br>"

    ret += "<b>Anotimp: </b>"
    ret += lib.biblioteca_fructe.anotimp_mango()
    ret += "<br>"

    print("DBG: apel obtine_mango")
    return ret

@app.route("/mango/culoare", methods=['GET'])
def obtine_culoare_mango():
    ret = ""
    ret += lib.biblioteca_fructe.culoare_mango()
    return ret

@app.route("/mango/gust", methods=['GET'])
def obtine_gust_mango():
    ret = ""
    ret += lib.biblioteca_fructe.gust_mango()
    return ret

@app.route("/mango/anotimp", methods=['GET'])
def obtine_anotimp_mango():
    ret = ""
    ret += lib.biblioteca_fructe.anotimp_mango()
    return ret

app.run(host = "127.0.0.1", port = 5002)
