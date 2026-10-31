import argparse
from pathlib import Path
from core import limpiar_registro_sensor, leer_json, escribir_json


def main()-> None:
    parser = argparse.ArgumentParser(description = "Limpia registros")
    
    parser.add_argument("entrada", type= Path, help= "Ruta al archivo JSON")
    
    parser.add_argument( "-o", "--output",
                        type=Path, default=Path("datos/registros_clean.json"),
                        help="Ruta archivo salida"
                    )
    args = parser.parse_args()
    
    registros_raw = leer_json(args.entrada)
    
    print(f"Leídos: {len(registros_raw)} registros de entrada")
    
    df_limpio = limpiar_registro_sensor(registros_raw)
                                        
    print(f"{len(df_limpio)} registros sanitizados")
                                            
                                     
    
    args.output.parent.mkdir(parents=True, exist_ok=True)
    registros_limpios = df_limpio.to_dict(orient="records")
    escribir_json(registros_limpios, args.output)
    print(f"Archivo guardado en: {args.output}")
    
    
    
if __name__== "__main__":
    main()