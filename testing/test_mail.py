import unittest #Importo la libreria para hacer los tests
from mail import enviar #Llamo a mail.py y importo la funcion enviar

class TestMail(unittest.TestCase): # Defino la clase TestMail para testear mail con la libreria correspondieste de test de python para hacer pruebas unitarias y verificar resultados
    def test_enviar(self): #Uso el self para acceder a los atributos y metodos, en este caso al usar unisttest convierte a test_enviar en un metodo de instancia
        emisor = "jonysanturio16@gmail.com" #Agregar mail donde hacer el testeo
        archivo = "Archivo_de_prueba.txt" #Nombre del archivo para hacer el testeo

        try:
            enviar(emisor, archivo) # Dentro de la funcion enviar de mail.py agrego las variables emisior, y archivo
            enviado = True # Esto es siempre y cuando se envié el correo
        except Exception as ex: # En caso de Error, el envio es falso y toma error al no enviar mail
            enviado = False
            print(f"Error al enviar correo: {ex}")
        
        self.assertTrue(enviado, "El correo no se envió correctamente") #El self.assertTrue se encarga de verificar que si es true, y si pasa algo toma error, para este caso no se envio el mail correctamente

if __name__ == "__main__":
    unittest.main()

