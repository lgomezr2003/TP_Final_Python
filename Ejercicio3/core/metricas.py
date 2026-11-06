""" Procesa métricas de consumo por planta"""

from core.emisiones import calcular_emisiones_carbono



def obtener_metricas_consumo(registros: list[dict]) -> dict:
    """ Procesa historial de consumo"""
    
    if not registros:
        return {
            "total_emisiones": 0.0,
            "planta_mayor_consumo": None,
            "detalle": [],
        }
    
    detalle = []
    total_emisiones = 0.0
    mayor_consumo = -1.0
    planta_mayor = None
    
    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        
        detalle.append({
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones": emisiones,
        })
        
        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor = planta
            
        return {
            "total_emisiones": round(total_emisiones, 2),
            "planta_mayor_consumo": planta_mayor,
            "detalle": detalle,
        }