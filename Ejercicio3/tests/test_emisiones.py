import unittest
from core.emisiones import calcular_emisiones_carbono

# Casos de exactitud 
class TestCalculoEmisiones(unittest.TestCase):
    """Casos de prueba para calcular emisiones de carbono"""
    
    def test_calculo_nominal(self) -> None:
        """ 100 Kwh con factor 0.4 -> 40-0 kg de CO2"""
        self.assertAlmostEqual(
            calcular_emisiones_carbono(100, 0.4), 40.0
        )
    def test_calculo_con_factor_personalizado(self) -> None:
        """ 200 Kwh con factor 0.5 -> 100.0 kg CO2"""
        self.assertAlmostEqual(calcular_emisiones_carbono(200, factor_emision=0.5), 100.0
        )
        
    def test_calculo_consumo_cero(self) -> None:
        """ 0 Kwh -> 0.0 kg CO2"""
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)
        
    def test_calculo_decimal(self) -> None:
        """12.5 Kwh con factor 0.4 -> 5.0 kg CO2"""
        self.assertAlmostEqual(
            calcular_emisiones_carbono(12.5, 0.4), 5.0
        )

# Casos de excepción

    def test_consumo_negativo_lanza_error(self) -> None:
        """ Consumo negativo -> ValueError"""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)
            
    def test_consumo_negativo_mensaje(self) -> None:
        """ El mensaje de error menciona el valor recibido """
        with self.assertRaises(ValueError) as ctx:
            calcular_emisiones_carbono(-5)
            self.assertIn("-5", str(ctx.exception))
            
if __name__ == "__main__":
    unittest.main()