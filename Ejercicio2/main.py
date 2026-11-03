"""Bloque de prueba"""
from pathlib import Path


from core import (
    StockInvalidoError,
    DispositivoEcologico,
    PanelSolar,
    GestorInventario,
    
)

def main() -> None:
    #Creo productos
    catalogo = [
        PanelSolar(modelo="EcoSun-100", precio=150.0, stock=10,
                   potencia_w=100, eficiencia=18.5),
        PanelSolar(modelo="EcoSun-250", precio=320.0, stock=5,
                   potencia_w=250, eficiencia=20.0),
        DispositivoEcologico(modelo="Bateria Eco", precio=200.0, stock=3),
    ]
    
    # muestra error
    print("Probando asignación de sctock inválido")
    try:
        catalogo[0].stock = -5
        print("Error -stock negativo-")
    except StockInvalidoError as e:
        print(f"Error capturado: {e}")
        print(f"Valor recibido: {e.valor_recibido}")
        
    # exportar catálogo
    ruta_salda = Path("datos/catalogo_ecotech.json")
    GestorInventario.guardar_catalogo_json(catalogo, str(ruta_salda))
    print(f"\n Catálogo gurdado en: {ruta_salda}")
    
    # muestro fichas
    print("\n Fichas técnicas:")
    for d in catalogo:
        print("-" * 30)
        print(d.ficha_tecnica())
        
if __name__ == "__main__":
    main()