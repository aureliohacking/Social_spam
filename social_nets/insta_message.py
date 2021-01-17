from instagram_private_api import Client


def main(user, password, destinatarios):

    client = Client(user, password)
    for i in destinatarios:
        client.post_comment(i, 'Holis')
    client.logout()
    return
