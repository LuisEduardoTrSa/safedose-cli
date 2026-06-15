import sys
from pathlib import Path

# Add the parent directory to the path to allow src imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
 fix/correcao-bugs
import os
from unittest.mock import patch
from src.calculator import calcular_dosagem, consultar_medicamento_fda, salvar_historico

from unittest.mock import patch
from src.calculator import calcular_dosagem, consultar_medicamento_fda
 main


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

@patch("src.calculator.create_client")
@patch.dict("os.environ", {"SUPABASE_URL": "http://mock-url", "SUPABASE_KEY": "mock-key"})
def test_salvar_historico_com_credenciais(mock_create_client):
    salvar_historico("Ibuprofen", 50.0, 10.0)
    
    mock_create_client.assert_called_once_with("http://mock-url", "mock-key")
    # Garante que a tabela foi chamada
    mock_create_client.return_value.table.assert_called_once_with("prescricoes")
    mock_create_client.return_value.table.return_value.insert.assert_called_once()
    mock_create_client.return_value.table.return_value.insert.return_value.execute.assert_called_once()

@patch.dict("os.environ", clear=True)
def test_salvar_historico_sem_credenciais():
    # Não deve lançar erro e deve retornar cedo
    salvar_historico("Ibuprofen", 50.0, 10.0)
