def multiplicacao(a, b):
    return a * b

def test_multiplicacao():
    assert multiplicacao(2, 3) == 10  # ERRO!
    assert multiplicacao(-1, 1) == 1  # ERRO!
