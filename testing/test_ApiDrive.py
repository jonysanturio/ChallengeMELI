import unittest # Importo la libreria para hacer el tests
from ApiDrive import crear_archivo, buscar, privado # Importo el archivo drive junto a los archivos crear_archivo, buscar y privado

class TestApiDrive(unittest.TestCase): # Defino la clase TestApiDrive para testear ApiDrive con la libreria correspondieste de test de python para hacer pruebas unitarias y verificar resultados
    def test_crear_archivo(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_crear_archivo en un metodo de instancia
        id_folder = "1at2dCNFkan1i5okyV9r_G_MDSmhlu18O" #Agregar el ID de la cerpeta a testear
        id_archivo = crear_archivo("Prueba.txt", "HOLA MUNDO", id_folder) # Llamo a crear_archivo con un nombre de archivo, su contenido y la carpeta de destino 
        self.assertIsNotNone(id_archivo, "El archivo no se creó correctamente") # Si el ID no tiene nada, surge una falla con un mensaje

    def test_buscar(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_buscar en un metodo de instancia
        query = "'root' in parents and trashed = false" #Con el query hago la consulta para que busque archivos en la raiz de google drive
        resultados = buscar(query) #Llamo a buscar para que almacené los resultados del query
        self.assertIsInstance(resultados, list, "El resultado de buscar no es una lista") #Verifica que los resultados sean una lista (ya que en este caso me lo tiene que devolver de esa forma ya que lo estoy buscando), pero si no es una lista tira un mensaje

    def test_privado(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_privado en un metodo de instancia
        id_archivo = "ID_VALIDO_DE_ARCHIVO_PUBLICO" #Define el ID del archivo de Google Drive que debe  ser publico
        cambiado = privado(id_archivo) # Llamo a la funcion privado para que cambie el archivo de publico a privado
        self.assertTrue(cambiado, "El archivo no se cambió a privado") #Devuelve True, si no, si hay error tira mensaje

if __name__ == "__main__":
    unittest.main()
