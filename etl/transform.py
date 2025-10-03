import pandas as pd

def clean_data(df):

    """
    Función para limpiar los datos.
    """
    # renombrar columnas
    df.columns = ['id','cliente','producto','precio','cantidad','total']
    
    # Eliminar duplicados
    df = df.drop_duplicates()

    # Rellenar valores nulos con algo por defecto
    df = df.fillna(
        {
            'producto': 'desconocido',
            'precio': 0,
            'cantidad': 0
        }
    )
    #df = df.dropna()

    # 3. Convertir a números (si hay texto raro lo cambia por 0)
    df['cantidad']= pd.to_numeric(df['cantidad'], errors='coerce').fillna(0)
    df['precio']= pd.to_numeric(df['precio'], errors='coerce').fillna(0)

    # 4. quitar negativos
    df = df[(df["cantidad"] >= 0) & (df["precio"] >= 0)]

    # 5. recalcular total (seguro, usando datos ya limpios)
    df['total'] = df['cantidad'] * df['precio']

    # 6. crear columna iva
    df['iva'] = df['total'] * 0.16
    
    return df