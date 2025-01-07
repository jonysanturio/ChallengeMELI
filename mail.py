import smtplib #Uso la libreria de smtplib para poder enviar correos electronicos
from email.message import EmailMessage # Uso la libreria de Email Message para facilitar la creacion de correos y enviar mensajes
import os # Uso el os para facilitarme la crear funciones, como manipulacion de archivos en este caso
from dotenv import load_dotenv # Llamo al archivo env y importo a la libreria load_dotenv para usar las variables del archivo .env que son mas reservadas a la hora de declararlas en el codigo


load_dotenv()

def enviar(owner_email, archivo): # Defino la funcion enviar que contiene le mail del propietario y el archivo a enviar
    email = os.getenv('EMAIL_USER') # Uso os.getenv para que me de del archivo .env la variable EMAIL_USER
    password = os.getenv('EMAIL_PASSWORD')# Uso os.getenv para que me de del archivo .env la variable EMAIL_PASSWORD
    subject = "Cambio visibilidad" # Por ultimo declaro el subject como variable por el cambion de visibilidad
    
    message = EmailMessage()
    message.set_content(f"El archivo '{archivo}' se cambió a privado.")
    message['Subject'] = subject
    message['From'] = email
    message['To'] = owner_email

# Por este lado creo el mensaje con la libreria de Email Message
# Con el message.set_content hice que establesca un mensaje en el correo, indicando el contenido y diciendo que se cambio el tipo de archivo
# El subject indica el asunto del mensaje (en este caso cambio de visibilidad)
# El from = email es el que remite el correo del propietario encargado de enviar esa notificacion
# To = owner es para quien va a recibir ese mensaje, que en este caso como se indico el enunciado tiene que ser para el owner

    try:
        print(f"Enviando correo a {owner_email} desde {email}...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(message)
        print(f"Correo enviado a {owner_email} con éxito.")
    except Exception as ex:
        print(f"Error al enviar el correo: {ex}")

# Esta parte la exprese de forma que envie correctamente el mail, en si uso una conexion de SMTP de Gmail para una conexion
# Por otro lado el SMTP tengo el email y password para la direccion de correo y la contraseña
# Luego uso el message para contener la informacion del correo y enviarlo asi mismo utilizando el SMTP
# En ese caso si el correo se envió se imprime un mensaje indicando que se envio con exito, sino que imprima otro mensaje indicando que ERROR
    