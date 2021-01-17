import os
from colorama import init
from colorama import Fore
from instabot import Bot
from instagram_private_api import Client
from stdiomask import getpass

init()


def comment(user, password, destinatarios, msj, max_comments):

    client = Client(user, password)
    cont = 0
    for i in destinatarios:
        if cont == max_comments:
            break
        else:
            try:
                client.post_comment(i, msj)
            except Exception as e:
                print(Fore.CYAN + '[INFO] No se pudo enviar a: ' +
                      Fore.YELLOW + str(e))
        cont += 1
    client.logout()
    print(Fore.CYAN + '[INFO] Finished')
    return


def main():

    os.system('cls')

    user = input(Fore.YELLOW + "[Paso 1/4] " + Fore.CYAN +
                 "Correo de la cuenta" + Fore.YELLOW + "\n-> ")
    password = getpass(Fore.YELLOW + "[Paso 2/4] " + Fore.CYAN +
                       "Contraseña de la cuenta" + Fore.YELLOW + "\n-> ")
    msj = input(Fore.YELLOW + "[Paso 3/4] " + Fore.CYAN +
                "Mensaje a enviar" + Fore.YELLOW + "\n-> ")
    max_comments = input(Fore.YELLOW + "[Paso 4/4] " + Fore.CYAN +
                         "Número máximo de comentarios" + Fore.YELLOW + "\n-> ")

    client = Client(user, password)
    userid = client.authenticated_user_id
    rank_token = client.generate_uuid()

    destinatarios = []
    publicaciones = []
    publicaciones_aux = []

    users = client.user_following(userid, rank_token)['users']
    for i in users:
        contact = i['pk']
        destinatarios.append(contact)

    print(destinatarios)
    client.logout()

    bot = Bot()
    bot.login(username=user, password=password, use_cookie=False)

    for i in destinatarios:
        publicaciones_aux = bot.get_user_medias(user_id=i,
                                                is_comment=True)
        publicaciones.append(publicaciones_aux[0])
    bot.logout()

    print(publicaciones)
    comment(user, password, publicaciones, msj, max_comments)

    print(Fore.WHITE)
    os.system('pause')
