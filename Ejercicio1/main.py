


import argparse
import sys
from pathlib import Path

from core import limpiar_registro_sensor, leer_json, escribir_json, generar_resumen_sensores


def main()-> None:
    
# Punto A    
    # Variables que se ingresan por comando
    parser = argparse.ArgumentParser(description = "Limpia registros")
    
    parser.add_argument("entrada", type= Path, help= "Ruta al archivo JSON")
    
    parser.add_argument( "-o", "--output",
                        type=Path, default=Path("datos/registros_clean.json"),
                        help="Ruta archivo salida"
                    )
    
    parser.add_argument ( "-u", "--umbral", type=float,
                         default=22.0,
                         help= "Temperatura límite para alerta. Default: 22.0")
    
    args = parser.parse_args()
    
    try:
        # Leo archivo .json de la carpeta datos o la indicada en las opciones.
        registros_raw = leer_json(args.entrada)
        
        print(f"Leídos: {len(registros_raw)} registros de entrada")
        
        # ejecto la normalización de los registros, limpianndo espacios y sufijos
        df_limpio = limpiar_registro_sensor(registros_raw)
                                            
        print(f"{len(df_limpio)} registros sanitizados")
                                                                    
        args.output.parent.mkdir(parents=True, exist_ok=True)
        registros_limpios = df_limpio.to_dict(orient="records")
        
        # persiste la salida de la uncion en un archivo .json en la carpeta datos o donde se especifique
        
        escribir_json(registros_limpios, args.output)
        print(f"Archivo guardado en: {args.output}")
        
        #print(f"contenido variable registros_limpios: {registros_limpios}")

    # Punto B
        # funcion de estadisticas, saca promedio, lista las lecturas fuera del umbral
        ids_alerta, promedio = generar_resumen_sensores(registros_limpios, args.umbral)
        #print(f" Promedio: {promedio}")
        
        #print(f"listado de tumplas fuera rango: {ids_alerta}")
    # Genera informe

        print("\n" + "=" * 45)
        print("   Reporte de Monitoreo de Sensores")
        print("=" * 45)
        print(f"Umbral de Alerta: {args.umbral}ºC")
        print(f"Promedio general: {promedio:.2f}ºC")
        print(f"\nSensores en alerta {len(ids_alerta)}:")
        if ids_alerta:
            for sensor_id in ids_alerta:
                print(f"  {sensor_id}")
        else:
            print(" (ninguno)")
        print("=" * 45)
    except FileNotFoundError:
        print("Ruta inexistente.")
        return 1
    except ValueError as e:
        print("Error de datos: {e}")
        return 1
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return 1
    
    
if __name__== "__main__":
    sys.exit(main())