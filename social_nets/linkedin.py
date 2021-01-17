import linkedin_api
import os
from colorama import init
from colorama import Fore
from stdiomask import getpass
from tkinter import *
from tkinter import filedialog

init()


def send():

    os.system('cls')

    user = input(Fore.YELLOW + "[Paso 1/4] " + Fore.CYAN +
                 "Correo de la cuenta" + Fore.YELLOW + "\n-> ")
    password = getpass(Fore.YELLOW + "[Paso 2/4] " + Fore.CYAN +
                       "Contraseña de la cuenta" + Fore.YELLOW + "\n-> ")
    msj = input(Fore.YELLOW + "[Paso 3/4] " + Fore.CYAN +
                "Mensaje a enviar" + Fore.YELLOW + "\n-> ")

    login = linkedin_api.Linkedin(user, password)

    print(Fore.YELLOW + "[Paso 4/4] " + Fore.CYAN +
          "Elige el  archivo  con  los destinatarios"
          "\n[Paso 4/4] (Si   cancelas  el  proceso,  el  mensaje"
          "\n[Paso 4/4] será  enviado  a  todos  los   contactos)" +
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

    destinatarios = []

    if file_path:
        print(Fore.YELLOW + '[INFO] ' + Fore.CYAN + 'Spam dirigido')
        with open(file_path, 'r') as f:
            for i in f.readlines():
                contact = (i.replace('\n', '').
                           replace('\t', '').
                           replace('\r', '').
                           replace(' ', '')
                           )

                destinatarios.append(contact)
    else:
        print(Fore.YELLOW + '[INFO] ' + Fore.CYAN + 'Spam no dirigido')

        conversations = login.get_conversations()['elements']
        for i in conversations:
            contact = i['entityUrn'].replace('urn:li:fs_conversation:', '')
            destinatarios.append(contact)

    for conversation in destinatarios:
        try:
            login.send_message(message_body=msj,
                               conversation_urn_id=conversation,
                               recipients=None)
        except Exception as e:
            print(Fore.CYAN + '[INFO] No se pudo enviar a: ' +
                  Fore.YELLOW + str(e))

    print(Fore.WHITE)
    os.system('pause')
    return
