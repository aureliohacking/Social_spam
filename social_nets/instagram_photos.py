import os
from instabot import Bot
from tkinter import *
from tkinter import filedialog


def send():

    # Para seleccionar la imagen
    os.system('cls')
    print('Paso 1/3: Seleccione una foto')
    os.system('pause')

    root = Tk()  # Iniciamos la ventana de la app
    photo_path = filedialog.askopenfilename(
                initialdir="/",
                title="Select a File",
                filetypes=(("jpeg files", "*.jpg"),
                           )
                )
    root.withdraw()  # Cerramos la ventana

    if not photo_path:
        print('Debe seleccionar una foto')
        os.system('pause')
        return

    # Para seleccionar el archivo con las cuentas
    print('Paso 2/3: Seleccione el archivo con las cuentas')
    os.system('pause')

    root = Tk()  # Iniciamos la ventana de la app
    file_path = filedialog.askopenfilename(
                initialdir="/",
                title="Select a File",
                filetypes=(("Text files", "*.txt"),
                           )
                )
    root.withdraw()  # Cerramos la ventana

    if not file_path:
        print('Debe seleccionar un archivo de texto')
        os.system('pause')
        return

    msj = input("Paso 3/3: Ingresa el msj que quieres enviar: ")

    # Creamos el vector con las cuentas
    with open(file_path, 'r') as f:

        for i in f.readlines():
            account = (i.replace('\n', '').
                       replace('\t', '').
                       replace('\r', '')
                       )

            user, password = account.split(' ')
            print('\nUser: ' + str(user) +
                  '\nPassword: ' + str(password) +
                  '\nFile_Path: ' + str(photo_path))

            # Publicamos el phishing con las cuentas objetivo

            try:
                bot = Bot()
                bot.login(username=user, password=password)
                bot.upload_photo(photo_path, caption=msj)
            except:
                bot.logout()
            bot.logout()

    os.system('pause')
