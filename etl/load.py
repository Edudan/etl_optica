import sqlite3
from etl.config import DB_FILEPATH

def load_data(df):
    '''
    cargamos el df nuevo a la base de datos
    '''
    conn = sqlite3.connect(DB_FILEPATH)
    df.to_sql('ventas', conn, if_exists='replace', index=False)
    conn.close()
    