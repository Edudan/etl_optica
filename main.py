from etl.extract import extract_data
from etl.transform import clean_data
from etl.load import load_data

if __name__ == "__main__":
    df = extract_data()
    print("✅ Primeras filas:")
    print(df.head())
    df_clean = clean_data(df)
    print("✅ Filas limpias:")
    print(df_clean.head())
    df_load = load_data(df_clean)
    print("✅ Datos cargados en la base de datos correctamente.")
    