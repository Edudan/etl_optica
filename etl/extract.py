import pandas as pd
import os
from etl.config import DATA_FILEPATH

def extract_data():
    """
    Función para extraer los datos del archivo CSV.
    """
    if not os.path.exists(DATA_FILEPATH):
        raise FileNotFoundError(f"El archivo {DATA_FILEPATH} no existe.")
    
    data = pd.read_csv(DATA_FILEPATH)
    
    return data


