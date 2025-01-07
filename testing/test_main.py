import unittest # Importo la libreria para hacer los tests
from main import main # Llamo al archivo main.py y importo la funcion main

class TestMain (unittest.TestCase): # Defino la clase TestMain para testear el main con la libreria correspondieste de test de python para hacer pruebas unitarias y verificar resultados
    def test_main(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_main en un metodo de instancia
        try:
            main() # Ejecutó la funcion main
            ejecutar = True # Ejecuto la variable ejecutar cuando sea verdadera
        except Exception as ex: 
            ejecutar = False #Sino, si hay algun error, su ejecucion es falsa
            print("ERROR:  {ex}")
        self.assertTrue(ejecutar, "No se ejecuto") #Verifica que ejecutar sea True, sino si falla devuelve que no se ejecuto

if __name__ == "__main__":
    unittest.main()