import os
from colorama import init
from colorama import Fore
from phishing import menu
from social_nets import facebook
from social_nets import instagram
from social_nets import linkedin
from social_nets import mail
from social_nets import twilio
from social_nets import twitter

init()

if True:

    menu_char = (Fore.YELLOW + '[M' +
                 Fore.CYAN + 'E' +
                 Fore.BLUE + 'N' +
                 Fore.RED + 'U]' + Fore.YELLOW)

    while True:

        os.system('cls')


        print(Fore.YELLOW + """
*****************************************************************************************
*  ____  ____   _    __  __   ____   ___   ____ ___    _    _       _   _ _____ _____   *
* / ___||  _ \ / \  |  \/  | / ___| / _ \ / ___|_ _|  / \  | |     | \ | | ____|_   _|  *""" + Fore.CYAN + """
* \___ \| |_) / _ \ | |\/| | \___ \| | | | |    | |  / _ \ | |     |  \| |  _|   | |    *
*  ___) |  __/ ___ \| |  | |  ___) | |_| | |___ | | / ___ \| |___  | |\  | |___  | |    *""" + Fore.RED + """
* |____/|_| /_/   \_\_|  |_| |____/ \___/ \____|___/_/   \_\_____| |_| \_|_____| |_|    *
*                                                                                       *
*****************************************************************************************
""" + Fore.CYAN + """
Creado por:  Aurelio Hacking                                              Version 1.0
""" + Fore.WHITE + """
Hola, vamos a hacer mucho spam hoy ((((̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅))))
""", end="")
        print(Fore.YELLOW +
"""
╔═════════════════╗
║*****************║
║*****=""" + menu_char + """=****║
║*****************║
""", end="")
        print(Fore.CYAN +
'║' + 'ESCOGE UNA OPCIÓN║' +
'\n║' + Fore.YELLOW + '[1]' + Fore.CYAN + ' Facebook' + '     ║'
'\n║' + Fore.YELLOW + '[2]' + Fore.CYAN + ' Instagram' + '    ║'
'\n║' + Fore.YELLOW + '[3]' + Fore.CYAN + ' Linkedin' + '     ║'
'\n║' + Fore.YELLOW + '[4]' + Fore.CYAN + ' Mail' + '         ║'
'\n║' + Fore.YELLOW + '[5]' + Fore.CYAN + ' Twilio' + '       ║'
'\n║' + Fore.YELLOW + '[6]' + Fore.CYAN + ' Twitter' + '      ║'
'\n║' + Fore.YELLOW + '[7]' + Fore.CYAN + ' Phishing' + '     ║'
'\n║' + Fore.YELLOW + '[0]' + Fore.CYAN + ' Exit         ║', end="")
        print(Fore.RED + """
║*****************║
║*****************║
║*****************║
╚═════════════════╝
""")


        choice = input(Fore.YELLOW + '\n-> ')

        try:
            choice = int(choice)
        except ValueError:
            continue

        # Para facebook
        if choice == 1:
            try:
                facebook.send()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para instagram
        elif choice == 2:
            try:
                instagram.main()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para linkedin
        elif choice == 3:
            try:
                linkedin.send()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para mail
        elif choice == 4:
            try:
                mail.send()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para msm con twilio
        elif choice == 5:
            try:
                twilio.send()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para msm con tter
        elif choice == 6:
            try:
                twitter.send()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para el phishing
        elif choice == 7:
            try:
                menu.start()
            except Exception as e:
                print(Fore.RED + '[WARNING] ' + str(e))
                print(Fore.WHITE)
                os.system("pause")

        # Para salir
        elif choice == 0:
            print(Fore.CYAN + '[INFO] Ejecución terminada...')
            exit()
