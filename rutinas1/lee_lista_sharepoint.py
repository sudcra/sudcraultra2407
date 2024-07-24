import pyodbc
import pandas as pd
from agrega_registros import agregar_registros

def imagenes_list(ultimo_leido):
    db_path = r'C:\sudcraultra_access\lista.accdb'

    try:
        # Conecta a la base de datos
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path)
        # Consulta SQL

        query = "SELECT * FROM hojas where id_lista >" + str(ultimo_leido)

        # Ejecuta la consulta
        cursor = conn.cursor()
        cursor.execute(query)

        # Lee los resultados en un DataFrame
        df = pd.read_sql_query(query, conn)

        # Cierra la conexión
        conn.close()

        # Ahora puedes trabajar con el DataFrame 'df'
        print(df)
        nombre_hoja = 'imagenes'
        agregar_registros(df,nombre_hoja,[])
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        print(f"Hubo un error al ejecutar la consulta: {sqlstate}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    imagenes_list(66)