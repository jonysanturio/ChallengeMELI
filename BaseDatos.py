import sqlite3 #Importo la libreria de SQLite3 
import os #Importo el modulo os para buscar variables de entornos. 
from dotenv import load_dotenv  #Importo el archivo .env para los datos privados sobre el usuario, la base de datos, y sobre el id del cliente de google drive

load_dotenv() # Llamo a load_dotenv para importar sobre el archivo .env

DB_PATH = os.getenv("DB_PATH", "basedatos.db") #En este caso llamo a la variable de entorno de DB_PATH que esta sobre el .env llamando al nombre de la base de datos basedatos.db
#os.getenv lo uso para las variables de entorno del SO, en este caso llamo del key a DB_PATH y a default (en caso de que no exista key) a la base de datos que la llame basedatos.db


def crear_tabla(): #Creo la funcion crear_tabla para crear las tablas de la base de datos 
    try: #Use try en el caso de que llegue a haber un error en ejecucion, caso en la base de datos y deje de ejecutarse en si. 
        with sqlite3.connect(DB_PATH) as conn: #Genero con el with un recurso seguro y automatico a la hora de que se conecte con la base de datos
            cursor = conn.cursor() # Creo una variable con el puntero cursor para interactuar con la base de datos
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS archivo (
                    nombre TEXT NOT NULL,
                    extension TEXT NOT NULL,
                    owner TEXT NOT NULL,
                    visibilidad TEXT CHECK(visibilidad IN ('publico', 'privado')) NOT NULL,
                    fecha_modificacion TEXT NOT NULL
                );
            ''') #Creo la base de datos en el caso de que no exista dicho nombre_de_archivo 
            conn.commit() # Guardo los cambios que fueron realizados en la base de datos con el conn.commit 
            print("Tabla 'archivo' creada o ya existente.")
    except sqlite3.Error as ex: #Luego el except para que indique si hay error en la base de datos y que indique que salió un error
        print(f"Error en la creación de la tabla: {ex}")

def guardar_datos(nombre, extension, owner, visibilidad, fecha_modificacion): #Declaro una función para que guarde los datos (junto a todos los especificados)
    try:
        with sqlite3.connect(DB_PATH) as conn: #Al momento de que el recurso sea seguro y automatico y me conecté a la base de datos
            cursor = conn.cursor() # Creo una variable con el puntero cursor para interactuar con la base de datos
            cursor.execute('''
                INSERT INTO archivo (nombre, extension, owner, visibilidad, fecha_modificacion)
                VALUES (?, ?, ?, ?, ?);
            ''', (nombre, extension, owner, visibilidad, fecha_modificacion)) # En este caso el INSERT lo utilizo para que me inserte datos en la base de datos y con el Value que me los devuelva, los  ? son para que me lo visualicen
            conn.commit() #Guardo los cambios que fueron realizados en la base de datos
            print(f"El archivo '{nombre}' se guardo en la base de datos.") # Muestro en pantalla el nombre del archivo insertado y para que lo visualice
    except sqlite3.Error as e: #En caso de error en la base de datos....
        print(f"Error al guardar los datos: {e}")

def obtener_archivos(): # Funcion para obtener archivos, en este caso lo uso para obtener los datos especificos del archivo o los archivos 
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor() # Creo una variable con el puntero cursor para interactuar con la base de datos
            cursor.execute('''
                SELECT * FROM archivo;
            ''')
            archivos = cursor.fetchall() # En este caso uso el SELECT para extraer todos los datos de la tabla de archivo y el cursor.fetchall es para que muestre o recupere todas las filas de la tabla de la base de datos
    except sqlite3.Error as e:
        print(f"Error al obtener los datos: {e}")
        return []

def actualizar_visibilidad(id_archivo, nueva_visibilidad): #Funcion para la visibilidad si es privada o publica, en este caso lo pido por base de ID unico del archivo y una nueva visualizacion
    try:
        with sqlite3.connect(DB_PATH) as conn: #Al momento de que el recurso sea correcto y automatico, que me conecté a la base de datos
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE archivo
                SET visibilidad = ?
                WHERE id = ?;
            ''', (nueva_visibilidad, id_archivo)) # Para este caso uso el UPDATE pra que me modifique o actualice el registro, luego el SET para que me modifique el valor de una columna que en este caso es visibilidad. Por ultimo uso el WHERE para una forma de consulta y que me consulte el tipo de ID, y esto me devuelva los datos de ID_archivo y nueva visibilidad
            conn.commit()
            print(f"EL archivo con ID {id_archivo} ahora es '{nueva_visibilidad}'.") 
    except sqlite3.Error as ex: # En caso de error en la base de datos.....
        print(f"Error al actualizar la visibilidad: {ex}")
