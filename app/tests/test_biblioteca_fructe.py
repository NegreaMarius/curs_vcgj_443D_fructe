import lib.biblioteca_fructe as b_fructe

def test_culoare_capsuni():
    culoare = b_fructe.culoare_capsuni()
    if culoare == 'rosu':
        assert True
    else:
        assert False

def test_gust_capsuni():
    gust = b_fructe.gust_capsuni()
    if gust == 'dulce':
        assert True
    else:
        assert False

def test_anotimp_capsuni():
    anotimp = b_fructe.anotimp_capsuni()
    if anotimp == 'toamna':
        assert True
    else:
        assert False        

