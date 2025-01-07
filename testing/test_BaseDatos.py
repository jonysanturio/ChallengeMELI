import unittest #Importo la libreria para hacer los tests
from BaseDatos import crear_tabla, guardar_datos, obtener_archivos #Llamo a BaseDatos.py y importo la funcion crear_tabla, guardar_datos, obtener_archivos

class TestBaseDatos(unittest.TestCase): # Defino la clase TestBaseDatos para testear BaseDatos con la libreria correspondieste de test de python para hacer pruebas unitarias y verificar resultados
    def test_crear_tabla(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_crear_tabla en un metodo de instancia
        try:
            crear_tabla() #Llamo a la funcion crear_tabla
            creada = True #En caso de que sea True es porque se creó la tabla
        except Exception as ex:
            creada = False #Sino, tira mensaje con error
            print(f"Error al crear tabla: {ex}")
        self.assertTrue(creada, "La tabla no se creó correctamente") #Es True, sino pasa algo toma error y manda un mensaje

    def test_guardar_datos(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_guardar_datos en un metodo de instancia
        try:
            guardar_datos("Prueba.txt", ".txt", "jonysanturio16@gmail.com", "privado", "2025-01-01") # Llamo a guardar_datos con los datos a probar, en este caso en el gmail.com se tiene que poner el mail asosiado a la prueba
            guardado = True # Si es True, los datos se guardaron correctamente
        except Exception as ex:
            guardado = False # Sino ocurre un false tirando error con un mensaje
            print(f"Error al guardar datos: {ex}")
        self.assertTrue(guardado, "Los datos no se guardaron correctamente") #Es True, sino pasa algo toma error y manda un mensaje

    def test_obtener_archivos(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_obtener_archivos en un metodo de instancia
        archivos = obtener_archivos() # Llamo a obtener_archivos y que almacene el resultado en la variable archivos
        self.assertIsInstance(archivos, list, "Los datos obtenidos no son una lista") #Verifica que los resultados sean una lista (ya que en este caso me lo tiene que devolver de esa forma ya que lo estoy buscando), pero si no es una lista tira un mensaje

if __name__ == "__main__":
    unittest.main()
