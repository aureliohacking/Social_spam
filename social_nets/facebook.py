import fbchat
import os
from colorama import init
from colorama import Fore
from fbchat import Client
from fbchat import _message
from fbchat import _thread
from stdiomask import getpass
from tkinter import *
from tkinter import filedialog

# Para arreglar un ISSUE de fbchat
import re
fbchat._util.USER_AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2)"
                            " AppleWebKit/537.36 (KHTML, like Gecko)"
                            " Chrome/86.0.4240.75 Safari/537.36"
                            ]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

init()


def send():

    os.system('cls')

    user = input(Fore.YELLOW + "[Paso 1/4] " + Fore.CYAN +
                 "Correo de la cuenta" + Fore.YELLOW + "\n-> ")
    password = getpass(Fore.YELLOW + "[Paso 2/4] " + Fore.CYAN +
                       "Contraseña de la cuenta" + Fore.YELLOW + "\n-> ")
    msj = input(Fore.YELLOW + "[Paso 3/4] " + Fore.CYAN +
                "Mensaje a enviar" + Fore.YELLOW + "\n-> ")

    print(Fore.YELLOW + "[Paso 4/4] " + Fore.CYAN +
          "Elige el  archivo  con  las cuentas " +
          Fore.YELLOW + "\n[Paso 4/4]" +
          Fore.CYAN + " (Si cancelas el proceso, el mensaje " +
          Fore.YELLOW + "\n[Paso 4/4]" +
          Fore.CYAN + " será enviado a todos los  contactos)" +
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

    client = Client(user,
                    password,
                    user_agent=None,
                    max_tries=1,
                    session_cookies=None
                    )

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
        for i in client.fetchAllUsers():
            contact = i.uid
            destinatarios.append(contact)
            print(i.uid, i.first_name)

    # for i in client.fetchAllUsers():
    #     print(i.uid, i.first_name)

    # print(Fore.WHITE)
    # os.system('pause')
    # return

    for destinatario in destinatarios:
        try:
            client.send(_message.Message(text=msj),
                        thread_id=destinatario,
                        thread_type=_thread.ThreadType.USER
                        )
        except Exception as e:
            print(Fore.CYAN + '[INFO] No se pudo enviar a: ' +
                  Fore.YELLOW + str(e))

    # client.logout() está presentando un error con la
    # función group()
    print(Fore.WHITE)
    os.system('pause')
