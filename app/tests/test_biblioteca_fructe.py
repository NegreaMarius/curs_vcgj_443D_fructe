import lib.biblioteca_fructe as b_fructe

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
