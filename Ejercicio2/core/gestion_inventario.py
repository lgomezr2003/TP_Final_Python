"""Gestión del catálogo y persistencia"""

import json
from pathlib import Path
from core.dispositivos import DispositivoEcologico


class GestorInventario:
    """ Persiste los datos del catálogo en disco"""
    
    @staticmethod
    def guardar_catalogo_json(
        lista_dispositivos: list[DispositivoEcologico],
        ruta_archivo: str
        ) -> None:
        """ lista dispositivos y guarda en disco
        argumentos: lista_dispositivos, ruta_archivo"""
        
        datos = [dispositivo_a_dict(d) for d in lista_dispositivos]
        
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
            
            
def dispositivo_a_dict(dispositivo: DispositivoEcologico) -> dict:
    """Convierte a diccionario"""
    datos= {
        "tipo": type(dispositivo).__name__,
        "modelo": dispositivo.modelo,
        "precio": dispositivo.precio,
        "stock": dispositivo.stock,
    }
    
    if hasattr(dispositivo, "potencia_w"):
        datos["potencia_w"] = dispositivo.potencia_w
        datos["eficiencia"] = dispositivo.eficiencia
    return datos