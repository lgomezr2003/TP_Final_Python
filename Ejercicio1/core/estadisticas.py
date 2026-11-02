


def generar_resumen_sensores(lista_sensores_limpios: list[dict], umbral_temperatura: float) -> tuple[id,float]:
    
    if not lista_sensores_limpios:
        raise ValueError("No existen registros para procesar")
    
    try:
    
        en_alerta = [s for s in lista_sensores_limpios if s["temperatura"] > umbral_temperatura]
                    
        ids_alerta = [s["sensor_id"] for s in en_alerta ]
        
        if lista_sensores_limpios:
            
            promedio = sum(s["temperatura"] for s in lista_sensores_limpios) / len(lista_sensores_limpios)
            #print(f"Listado de tuplas en estadísticas: {lista_sensores_limpios}")
        
        else:
            
            promedio = 0.0
        return ids_alerta, promedio
    except KeyError as e:
        print(f"Error: temperatura no numérica")
        print(f"detalle: {e}")
        raise