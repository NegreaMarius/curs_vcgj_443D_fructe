import lib.biblioteca_fructe as b_fructe

'''
 ------------------------------------
    #0. CRChende - Afine
 ------------------------------------
'''

def test_culoare_afine():
    cul = b_fructe.culoare_afine()
    if cul == 'mov':
        assert True
    else:
        assert False

def test_gust_afine():
    inf = b_fructe.gust_afine()
    if inf == 'dulce':
        assert True
    else:
        assert False

def test_anotimp_afine():
    inf = b_fructe.anotimp_afine()
    if inf == 'vara':
        assert True
    else:
        assert False
        
'''
 ------------------------------------
    #10. NEGREA M. Marius-Ştefan - rodie
 ------------------------------------
'''

def test_culoare_rodie():
    cul = b_fructe.culoare_rodie()
    if cul == 'rosu':
        assert True
    else:
        assert False

def test_gust_rodie():
    inf = b_fructe.gust_rodie()
    if inf == 'dulce_acrisor':
        assert True
    else:
        assert False

def test_anotimp_rodie():
    inf = b_fructe.anotimp_rodie()
    if inf == 'toamna':
        assert True
    else:
        assert False

'''
 ------------------------------------
    #03. BĂNESCU A.F. Alexandru - capsuna
 ------------------------------------
'''

def test_culoare_capsuna():
    cul = b_fructe.culoare_capsuna()
    if cul == 'rosu':
        assert True
    else:
        assert False

def test_gust_capsuna():
    inf = b_fructe.gust_capsuna()
    if inf == 'dulce':
        assert True
    else:
        assert False

def test_anotimp_capsuna():
    inf = b_fructe.anotimp_capsuna()
    if inf == 'toamna':
        assert True
    else:
        assert False
