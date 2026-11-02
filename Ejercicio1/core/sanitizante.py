import pandas


def limpiar_registro_sensor(registros_raw: list[dict]) -> pandas.DataFrame:
    try:
        df = pandas.DataFrame(registros_raw)
        df["sensor_id"] = df["sensor_id"].str.strip()
        df["temperatura"] = df["temperatura"].str.rstrip("ºC").astype(float)
        df["ubicacion"] = df["ubicacion"].fillna("").str.strip()
        df["ubicacion"] = df["ubicacion"].fillna("No especificada")
        df.loc[df["ubicacion"].str.strip() == "", "ubicacion"] = "No especificada"
        
        return df
    except ValueError as e:
        print(f"Error al limpiar registros: {e}")
        print(" 'temperatura' no es un valor numérico")
    except AttributeError as e:
        print(f" Error: valor inesperado en 'temperatura'")
        print(f"Detalle: {e}")
        raise
