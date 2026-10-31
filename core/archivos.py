import json

def leer_json(ruta: str) -> list[dict]:
    
    with open(ruta, "r", encoding = "utf-8") as archivo:
        return json.load(archivo)
    
def escribir_json(datos: list[dict], ruta: str) -> None:
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)