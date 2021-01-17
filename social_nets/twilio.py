import os
from colorama import init
from colorama import Fore
from twilio.rest import Client
from tkinter import *
from tkinter import filedialog
from stdiomask import getpass

init()


def send():

    os.system('cls')
    print(Fore.YELLOW + "[Paso 1/5] " + Fore.CYAN +
          "Elige el  archivo  con  los destinatarios" +
          Fore.YELLOW + "\n-> ")
    print(Fore.WHITE)
    os.system('pause')

    root = Tk()  # Iniciamos la ventana de la app
    file_path = filedialog.askopenfilename(
                initialdir="/",
                title="Select a File",
                filetypes=(("Text files", "*.txt*"),
                           )
                )
    root.withdraw()  # Cerramos la ventana

    if not file_path:
        print(Fore.YELLOW + '[INFO] ' + Fore.CYAN +
              'Debes seleccionar un archivo')
        print(Fore.WHITE)
        os.system('pause')
        return

    with open(file_path, 'r') as f:

        destinatarios = []

        for i in f.readlines():
            contact = (i.replace('\n', '').
                       replace('\t', '').
                       replace('\r', '').
                       replace(' ', '')
                       )

            destinatarios.append(contact)

    account_sid = input(Fore.YELLOW + "[Paso 2/5] " + Fore.CYAN +
                        "account_sid" + Fore.YELLOW + "\n-> ")
    auth_token = getpass(Fore.YELLOW + "[Paso 3/5] " + Fore.CYAN +
                         "auth_token" + Fore.YELLOW + "\n-> ")
    num_from = input(Fore.YELLOW + "[Paso 4/5] " + Fore.CYAN +
                     "Número emisor" + Fore.YELLOW + "\n-> ")
    msj = input(Fore.YELLOW + "[Paso 5/5] " + Fore.CYAN +
                "Ingresa el msj que quieres enviar" + Fore.YELLOW + "\n-> ")
    client = Client(account_sid, auth_token)

    for destino in destinatarios:

        try:
            message = client.messages \
                .create(
                       body=msj,
                       from_=num_from,  # +18653445676
                       to=destino
                       )
        except:
            print(Fore.CYAN + '[INFO] No se pudo enviar a: ' +
                  Fore.YELLOW + str(message))

    print(Fore.CYAN + '[INFO] Finished')
    os.system('pause')
    print(Fore.WHITE)
    return
