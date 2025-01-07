
from pydrive2.auth import GoogleAuth # Llamo la libreria de Google
from pydrive2.drive import GoogleDrive # Llamo a la Api de drive junto a su libreria
import os # Uso el os para facilitarme la crear funciones, como manipulacion de archivos en este caso
from dotenv import load_dotenv # Llamo al archivo env y importo a la libreria load_dotenv para usar las variables del archivo .env que son mas reservadas a la hora de declararlas en el codigo
gauth = GoogleAuth() # Llamo a la libreria de google drive para que me abra la aplicacion
gauth.LocalWebserverAuth() # De esta forma me abre automaticamente la aplicacion al momento de compilarlo

#Creo una variable que contenga la nueva credencial
dir_credencial = 'credentials_module.json'


def sesion(): #Funcion para iniciar sesion a Google Drive
    try:
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(dir_credencial)
    
        if gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(dir_credencial)
        else:
            gauth.Authorize()
        return GoogleDrive(gauth)
    except Exception as ex:
        print(f"Error al autenticar: {ex}")
        return None
#En este caso lo hago para que este bien autenticado al momento de entrar, en ese caso uso un condicional para que si el token expira que cree uno nuevo y se actualice el archivo
#Y en el caso de que no, que directamente lo autentique.


def crear_archivo(nombre_archivo, contenido, id_folder): # Funcion de crear archivo con los contenidos especificos
    credenciales = sesion() # En este caso llamo a sesion que contiene todo de la API de Google Drive a una variable dir_credencial que luego me va a autenticar o tomar arhcivos, contenidos, id, etc
    if not credenciales: # Sino existe esa credencial tira mensaje de ERROR y me retorna a NONE
        print("Error: No se puede autenticar")
        return None
    archivo = credenciales.CreateFile({
        'title': nombre_archivo, 
        'parents':[{'kind': 'drive#fileLink','id': id_folder}] 
    }) # En este caso lo utlizo para que cree un archivo en Google Drive, y el metodo CreateFile recibe datos de title(nombre del archivo que aprece en Google Drive) y de parents(Lista que contiene la carpeta que se guarda en el archivo)
    archivo.SetContentString(contenido) # Establece el contenido del archivo que se va a subir, el SetContetnString toma cadena de textos que contiene en este caso (contenido) asignandole a un archivo
    archivo.Upload() # Actualiza el archivo de Google Drive
    print(f"Archivo '{nombre_archivo}' creado con exito. ID {archivo['id']}")
    return archivo['id'] #En este caso quiero que me devuelve unicamente el archivo con el ID unico, para no generar confuncion con demas archivos con el ID

    
def buscar(query): # Funcion de buscar archivo y contiene el query para mostrar todo el contenido raiz del archivo o carpeta de Google Drive
    resultado = [] #Creo una lista vacia para luego ir almacenando los archivos que se fueron encontrando
    credenciales = sesion()
    try:
        lista_archivos = credenciales.ListFile({'q': query}).GetList()
        for archivo in lista_archivos:
            print(f"Nombre: {archivo['title']}")
            print(f"ID: {archivo['id']}")
            print(f"Propietario: {archivo['owners'][0]['emailAddress'] if 'owners' in archivo and archivo['owners'] else 'No disponible'}")
            print(f"Visibilidad {'Publico' if 'anyone' in archivo.get('permissions', []) else 'Privado'}")
            print(f"Ultima modificacion: {archivo['modifiedDate']}\n")
            print(f"Permisos: {archivo.get('permissions', 'No disponible')}")
        resultado.append(archivo)
        return resultado
    except Exception as ex:
        print(f"Error al buscar: {ex}")
        return resultado
# En este caso con el ListFile con 'q' query busca los archivos que traten de conseguir a la hora de buscar el mismo
# Para ello generó un bucle for para que vaya recorriendo de forma recursiva los archivos de la lista_archivos
# De esa forma voy imprimiendo todas las especificaciones que se pide al momento de buscar un archivo, en el owners verifica el archivo si tiene propietario o de quien es mas que nada
# Para ello se le dice que si existe ese dato que imprima el correo del propietario sino que indique que no esta disponible el correo
# En visibilidad revisa los permisos del archivo y si es anyone (osea publico), indica que sea luego privado
# Luego en resultado.append agrega el archivo actual a la lista resultado
# Por ultimo que me devuelva resultado con todo el contendido que se encontro en el archivo.
    
def privado(id_archivo): # Funcion de visibilidad a privado junto al id_archivo
    credenciales = sesion()
    if not credenciales: # Sino existe esa credencial tira mensaje de error
        print("Error: No se pudo autenticar")
        return False
    try:
        archivo = credenciales.CreateFile({'id': id_archivo})
        permisos = archivo.GetPermissions()
        print(f"Permisos modificados: {permisos}")
        publico = False
        for permiso in permisos:
            if permiso['type'] == 'anyone':
                publico = True
                archivo.DeletePermission(permiso['id'])
                print(f"Permiso público eliminado ID {id_archivo}.")
        if publico:
            archivo.Upload()  # Actualiza el archivo en Drive
        return publico  # Devuelve True si era público
    except Exception as e:
        print(f"Error al cambiar permisos a privado: {e}")
        return False

# Para este caso en la variable archivo se le agrega la credencial de autenticacion para la referencia al archivo de Google Drive por su ID
# Para la variable permisos uso el GetPermissions para que me devuelva la lista de los permisos que esten asociados al archivo
# Por otro lado recorro de manera recursiva los permisos para que si encuentra alguno publico con el DeletePermission elimine el archivo publico
# Por otro lado en el caso de que sea un archivo publico (True) que actualice el archivo en Drive y me retorne a Publico, dependiendo si es True o False
# Caso de False que me imprima un mensaje de ERROR