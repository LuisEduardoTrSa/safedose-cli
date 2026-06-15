import unittest
 fix/correcao-bugs
from unittest.mock import patch

import sys
from pathlib import Path

# Add the parent directory to the path to allow src imports
sys.path.insert(0, str(Path(__file__).parent.parent))

 main
from src.calculator import consultar_medicamento_fda, calcular_dosagem

class TestSafeDose(unittest.TestCase):

    def test_calcular_dosagem_sucesso(self):
        self.assertEqual(calcular_dosagem(10, 50, 15), 3.0)

 fix/correcao-bugs
    @patch('src.calculator.requests.get')
    def test_integracao_openfda(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "openfda": {
                        "generic_name": ["IBUPROFEN"],
                        "brand_name": ["Advil"]

    def test_integracao_openfda(self):
        from unittest.mock import patch
        with patch('src.calculator.requests.get') as mock_get:
            mock_response = unittest.mock.Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "results": [
                    {
                        "openfda": {
                            "generic_name": ["IBUPROFEN"],
                            "brand_name": ["Advil"]
                        }
 main
                    }
                ]
            }
            mock_get.return_value = mock_response
            resultado = consultar_medicamento_fda("ibuprofen")
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado['generico'], "Ibuprofen")
            self.assertEqual(resultado['marca'], "Advil")
            mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
