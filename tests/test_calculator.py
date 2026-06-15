import pytest
from unittest.mock import patch
from src.calculator import calcular_dosagem, consultar_medicamento_fda

def test_calculo_dosagem_sucesso():

    assert calcular_dosagem(10, 100, 20) == 2.0

def test_calculo_dosagem_valor_invalido():
    with pytest.raises(ValueError, match="maiores que zero"):
        calcular_dosagem(0, 50, 10)

def test_calculo_dosagem_valor_limite():
    assert calcular_dosagem(0.5, 10, 5) == 0.25


@patch("src.calculator.requests.get")
def test_consultar_medicamento_fda(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": [
            {
                "openfda": {
                    "generic_name": ["Ibuprofen"],
                    "brand_name": ["Advil"]
                }
            }
        ]
    }

    resultado = consultar_medicamento_fda("ibuprofen")

    assert resultado["generico"] == "Ibuprofen"
    assert resultado["marca"] == "Advil"

@patch("src.calculator.requests.get")
def test_consultar_medicamento_fda_nao_encontrado(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": []
    }

    resultado = consultar_medicamento_fda("medicamento_inexistente")

    assert resultado is None
