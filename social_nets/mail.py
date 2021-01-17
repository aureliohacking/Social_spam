import os
import smtplib
import ssl
from colorama import init
from colorama import Fore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from stdiomask import getpass
from tkinter import *
from tkinter import filedialog

init()


def send():

    os.system('cls')
    print(Fore.YELLOW + "[Paso 1/4] " + Fore.CYAN +
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
        print(Fore.CYAN + '[INFO] Debes seleccionar un archivo')
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

    print(Fore.YELLOW + "[Paso 2/4] " + Fore.CYAN +
          "Elige el  archivo  con  la plantilla HTML" +
          Fore.YELLOW + "\n[Paso 2/4]" + Fore.CYAN +
          " (Si    cancelas    el     proceso,    se" +
          Fore.YELLOW + "\n[Paso 2/4]" + Fore.CYAN +
          " una   plantilla   por   defecto   usará)" +
          Fore.YELLOW + "\n-> ")
    print(Fore.WHITE)
    os.system('pause')

    root = Tk()  # Iniciamos la ventana de la app
    plantilla = filedialog.askopenfilename(
                initialdir="/",
                title="Select a File",
                filetypes=(("HTML", "*.html*"),
                           )
                )
    root.withdraw()  # Cerramos la ventana

    if not plantilla:
        phishing_link = input(Fore.YELLOW + "[Requerido] " + Fore.CYAN +
                              " Ingresa el link del phishing para" +
                              " la plantilla por defecto" +
                              Fore.YELLOW + "\n-> ")
        plantilla = """\
        <html>
          <body>
            <h1 style="color: deepskyblue;">
              PROYECTO DE SEGURIDAD
            </h1>
            <p style="color: darkred;">
              Hola,
              <a href=\"""" + phishing_link + """\" target="_blank">
               click aquí
              </a>
            </p>
          </body>
        </html>
        """
    else:
        with open(plantilla, 'r') as f:
            plantilla = f.read()

    user = input(Fore.YELLOW + "[Paso 3/4] " + Fore.CYAN +
                 "Correo de la cuenta" + Fore.YELLOW + "\n-> ")
    password = getpass(Fore.YELLOW + "[Paso 4/4] " + Fore.CYAN +
                       "Contraseña de la cuenta" + Fore.YELLOW + "\n-> ")

    message = MIMEMultipart("alternative")
    message["Subject"] = "SPAM TEST"
    message["From"] = user
    message["To"] = ', '.join(destinatarios)

    # Creamos los objetos con las partes del correo
    part1 = MIMEText(plantilla, "html")

    # Adjuntamos las partes del correo
    message.attach(part1)

    context = ssl.create_default_context()  # Con este context:
    # Se cargarán los certificados de CA de confianza del sistema.
    # Se habilitarán la verificación del nombre de host y,
    # la validación del certificado.
    # Y se intentará elegir un protocolo y una configuración de
    # cifrado razonablemente seguros.

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user, password)
        no_recibidos = server.sendmail(user,
                                       destinatarios,
                                       message.as_string()
                                       )
        print(Fore.CYAN + '[INFO] Finished')

    print(Fore.WHITE)
    os.system('pause')
    return
