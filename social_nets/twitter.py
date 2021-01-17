import os
import tweepy
from colorama import init
from colorama import Fore
from stdiomask import getpass
from tweepy import OAuthHandler

init()


def send():

    os.system('cls')

    # consumer_key = getpass("Paso 1/7: Ingresa tu Api_Key: ")
    # consumer_secret = getpass("Paso 2/7: Ingresa tu Api_Key Secreta: ")
    # access_token = getpass("Paso 3/7: Ingresa tu Access_Token: ")
    # access_token_secret = getpass("Paso 4/7: Ingresa tu Access_Token_Secreto: ")

    # consumer_key = 'VHUq8ThaGtCrvsnz2HuAxelLD'
    # consumer_secret = 'En9UWHS6L7ZUCGSmWmo66csod6gm8XV6CxIDyTKg1ihXsTxRoG'
    # access_token = '4705602896-LObnx0E8FK0Bcsky4eHl0M1vS1g8Hv7VGUi0YQN'
    # access_token_secret = '5IEgrOBDTHcuGOyjkgrQ2LYL1t2whOL1MxA23kY91OkJI'

    consumer_key = getpass(Fore.YELLOW + "[Paso 1/7] " + Fore.CYAN +
                           "consumer_key" + Fore.YELLOW + "\n-> ")
    consumer_secret = getpass(Fore.YELLOW + "[Paso 2/7] " + Fore.CYAN +
                              "consumer_secret" + Fore.YELLOW + "\n-> ")
    access_token = getpass(Fore.YELLOW + "[Paso 3/7] " + Fore.CYAN +
                           "access_token" + Fore.YELLOW + "\n-> ")
    access_token_secret = getpass(Fore.YELLOW + "[Paso 4/7] " + Fore.CYAN +
                                  "access_token_secret" + Fore.YELLOW + "\n-> ")

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Listos para hacer la conexion con el API
    api = tweepy.API(auth)

    objetive = input(Fore.YELLOW + "[Paso 5/7] " + Fore.CYAN +
                     "Ingresa el  nombre  de  la cuenta  objetivo" +
                     Fore.YELLOW + "\n[Paso 5/7]" + Fore.CYAN +
                     " (Presiona Enter si será la cuenta logueada)" +
                     Fore.YELLOW + "\n-> ")
    max_messages = input(Fore.YELLOW + "[Paso 6/7] " + Fore.CYAN +
                         "Ingresa el número máximo de contactos" +
                         Fore.YELLOW + "\n[Paso 6/7]" + Fore.CYAN +
                         " a los que se les enviará el mensaje" +
                         Fore.YELLOW + "\n-> ")
    msj = input(Fore.YELLOW + "[Paso 7/7] " + Fore.CYAN +
                "Mensaje" +
                Fore.YELLOW + "\n-> ")

    if not objetive:
        objetive = api.me()._json['id']

    destinatarios = api.followers_ids(objetive)

    print(objetive, end='\n\n')
    print(destinatarios)

    cont = 0
    for i in destinatarios:
        print('Mensaje ' + str(cont))
        if cont == int(max_messages):
            break
        else:
            try:
                api.send_direct_message(recipient_id=i, text=msj)
            except:
                print(Fore.CYAN + '[INFO] No se pudo enviar a: ' +
                      Fore.YELLOW + i)
        cont += 1

    print(Fore.CYAN + '[INFO] Finished')
    print(Fore.WHITE)
    os.system('pause')

    return


# api_key = VHUq8ThaGtCrvsnz2HuAxelLD
# api_key_secret = En9UWHS6L7ZUCGSmWmo66csod6gm8XV6CxIDyTKg1ihXsTxRoG
# access_token = 4705602896-LObnx0E8FK0Bcsky4eHl0M1vS1g8Hv7VGUi0YQN
# access_token_secret = 5IEgrOBDTHcuGOyjkgrQ2LYL1t2whOL1MxA23kY91OkJI
# bearer_token = AAAAAAAAAAAAAAAAAAAAADcxKQEAAAAA06jrVtMgiqQpdZcrGNXXzho%2FL58%3DM85kyQyp0sMzY61Xwkk6v8YW1mZpYwQ2aYTLrXcoSCR7vX4ATQ
