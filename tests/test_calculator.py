import pytest
from src.calculator import calcular_dosagem

def test_calculo_dosagem_sucesso():

    assert calcular_dosagem(10, 100, 20) == 2.0

def test_calculo_dosagem_valor_invalido():
    with pytest.raises(ValueError, match="maiores que zero"):
        calcular_dosagem(0, 50, 10)

def test_calculo_dosagem_valor_limite():
    assert calcular_dosagem(0.5, 10, 5) == 0.25
