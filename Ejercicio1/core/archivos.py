import json

def leer_json(ruta: str) -> list[dict]:
    try: #agrego try por los errores del json de entrada
        with open(ruta, "r", encoding = "utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error, no se encontró el archivo '{ruta}'")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: el archivo '{ruta}' no es un JSON válido")
        print(f" Detalle: {e}")
        print(f" Línea {e.lineno}, columna {e.colno}")
        raise
    
def escribir_json(datos: list[dict], ruta: str) -> None:
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)