""" Algoritmo de cálculo de emisiones"""


def calcular_emisiones_carbono(
    consumo_kwh: float,
    factor_emision: float = 0.4
) -> float:
    """ Calcula las emisiones de CO2 a partir del consumo eléctrico"""
    if consumo_kwh < 0:
        raise ValueError(
            f"El consumo no puede ser negativo: {consumo_kwh}"
        )
    return consumo_kwh * factor_emision