def soma(a, b):
    """Retorna a soma de dois números"""
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
