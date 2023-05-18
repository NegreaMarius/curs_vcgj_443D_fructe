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
'''
 ------------------------------------
    #04. BELIŢOIU F.M. Rareş-Florian - mar
 ------------------------------------
'''

def test_culoare_mar():
    cul = b_fructe.culoare_mar()
    if cul == 'verde':
        assert True
    else:
        assert False

def test_gust_mar():
    inf = b_fructe.gust_mar()
    if inf == 'dulce_acrisor':
        assert True
    else:
        assert False

def test_anotimp_mar():
    inf = b_fructe.anotimp_mar()
    if inf == 'toamna':
        assert True
    else:
        assert False
        
'''
 ------------------------------------
    #19. ŞPAN O. Lorin - vanata
 ------------------------------------
'''

def test_culoare_vanata():
    cul = b_fructe.culoare_vanata()
    if cul == 'mov':
        assert True
    else:
        assert False

def test_gust_vanata():
    inf = b_fructe.gust_vanata()
    if inf == 'dulce_acrisor':
        assert True
    else:
        assert False

def test_anotimp_vanata():
    inf = b_fructe.anotimp_vanata()
    if inf == 'vara':
        assert True
    else:
        assert False

'''
 ------------------------------------
    #25. VASILESCU P. Bogdan - piersica
 ------------------------------------
'''

def test_culoare_piersica():
    cul = b_fructe.culoare_piersica()
    if cul == 'portocaliu':
        assert True
    else:
        assert False

def test_gust_piersica():
    inf = b_fructe.gust_piersica()
    if inf == 'dulce':
        assert True
    else:
        assert False

def test_anotimp_piersica():
    inf = b_fructe.anotimp_piersica()
    if inf == 'vara':
        assert True
    else:
        assert False
        
        '''
 ------------------------------------
    #24. VASILE M. Vlad-Andrei - kiwi
 ------------------------------------
'''

def test_culoare_kiwi():
    cul = b_fructe.culoare_kiwi()
    if cul == 'verde':
        assert True
    else:
        assert False

def test_gust_kiwi():
    inf = b_fructe.gust_kiwi()
    if inf == 'sarat':
        assert True
    else:
        assert False

def test_anotimp_kiwi():
    inf = b_fructe.anotimp_kiwi()
    if inf == 'vara':
        assert True
    else:
        assert False
        
        
'''
 ------------------------------------
    #22. TUDOSE V.D. Bogdan-Mihai - portocala
 ------------------------------------
'''

def test_culoare_portocala():
    cul = b_fructe.culoare_portocala()
    if cul == 'portocaliu':
        assert True
    else:
        assert False

def test_gust_portocala():
    inf = b_fructe.gust_portocala()
    if inf == 'dulce_acrisor':
        assert True
    else:
        assert False

def test_anotimp_portocala():
    inf = b_fructe.anotimp_portocala()
    if inf == 'iarna':
        assert True
    else:
        assert False
