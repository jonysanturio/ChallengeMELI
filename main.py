from ApiDrive import privado, buscar, crear_archivo #Llamo al archivo ApiDrive.py y importo privado, buscar y crear_archivo
from BaseDatos import crear_tabla, guardar_datos #Llamo al archivo BaseDatos.py y importo crear_tabla y guardar_datos
from mail import enviar #Llamo al archivo mail.py y importo enviar
import os # Uso el os para facilitarme la crear funciones, como manipulacion de archivos en este caso
from dotenv import load_dotenv # Llamo al archivo env y importo a la libreria load_dotenv para usar las variables del archivo .env que son mas reservadas a la hora de declararlas en el codigo

def main():
    crear_tabla()
    
    #En esta parte mi logica plasmada fue que el archivo_prueba creado aparezca a su vez en el apartado principal del Google Drive y se visualice
    nombre_archivo = "archivo_prueba.txt" #Archivo_prueba va a aperecer en el main de Google Drive
    contenido = "Este es un archivo de prueba para verificar el funcionamiento."
    id_folder = "root"  # El root lo utilizo como identificador de la carpeta raiz para que cree el archivo y lo mande ahí.
    id_archivo_prueba = crear_archivo(nombre_archivo, contenido, id_folder) # Le asigno a una variable y llamo a crear_archivo junto a los contenidos especificos, nombre, contenido, id_folder

    query = "'root' in parents and trashed = false" # El query lo utilizo para que me busque todo los archivos raiz de Google Drive junto al root
    archivos = buscar(query) #Llamo a la funcion buscar junto que contenga el query (que contiene el root archivos raices para que me haga la busqueda general en Google Drive)

    if archivos: # Hago una verificacion en la variable archivo que contiene la funcion buscar
        for archivo in archivos: #Recorro cada elemento de archivo en la lista archivos
            print(archivo) #Me imprime el archivo actual
            owner_email = "Desconocido" #Deduci de que analice la variable se almacena en el correo del propietario del archivo, en su defecto si no se encuentra su correo, lo identifique como desconocido
            if 'owners' in archivo and isinstance(archivo['owners'], list) and archivo['owners']: # Si owners esta en archivo y que verifique si pertenece a un tipo o clase  (en este caso una lista) se fije si esta vacia o no. 
                owner_email = archivo['owners'][0].get('emailAddress', "Desconocido") # Si se cumple esa condicion, extrae el correo del propietario, y si no se encuentra se asigna Desconocido
            permisos = archivo.get('permissions', []) # Trato de obtener los permisos del archivo o en su defecto una lista vacia sino existe permissions (en su defecto permissions me brinda saber si representa a una lista de permisos asociados a un archivo)
            visibilidad = "publico" if any(p.get('type') == 'anyone' for p in permisos) else "privado" # Evaluó si algun permiso en la lista tiene type y/o anyone, en ese caso si no los tiene se le asigna privado
            
            guardar_datos( # En la funcion de guardar_datos unicamente guardo datos en la base de datos que sean especificos del propietario, del tipo de arhcivo, junto a su visibilidad y su fecha modificada
                nombre=archivo.get('title', 'Sin título'),
                extension=os.path.splitext(archivo.get('title', 'Sin título'))[1], # Utilizo extension para saber el tipo de archivo, en este caso el os.path.splitext lo uso para dividir el nombre del archivo, si es por nombre de archivo o extension del archivo y con [1] es para el tipo de indice de la extension del archivo.
                owner=owner_email,
                visibilidad=visibilidad,
                fecha_modificacion=archivo.get('modifiedDate', 'Fecha desconocida')# Uso el modifiedDate para la ultima fecha y hora para saber la modificacion de un archivo.
            )

            if visibilidad == "publico": # En el condicional, pregunto si la visibilidad es publica
                if privado(archivo['id']):  # Solo envía correo si el archivo es público
                    print(f"Archivo {archivo.get('title', 'Sin título')} Es privado.") #Imprime un mensaje indicando el tipo de archivo con el.get junto a un titulo o si no contiene titulo el archivo indicando que se paso a privado
                    enviar(owner_email, archivo.get('title', 'Sin título')) #Junto a eso llamo a la funcion enviar para que contenga el mail del owner junto al archivo que se le adjunta con el titulo o sin titulo y lo envia al mail del owner

if __name__ == "__main__":
    main()
    enviar("correo_propio@gmail.com", "archivo_prueba.txt") #Esto es una prueba para mostrar la funcionalidad del codigo y muestre realmente si funciona o no para que reciba la notificacion del correo
    