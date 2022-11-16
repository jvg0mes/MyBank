from msg.text import msg
from getpass import getpass
import shelve
from sec.spw import spw
from .Resultado import resultado
from services.database_service import database_service as db

class Login():

    def __init__(self):

        print(msg['login_main'])
        auth = self.__requireCredentials()
        if (auth.resultado):
            print("\nBem-vindo " + auth.mensagem + "!")
        else:
            print("\n" + auth.mensagem)

    @classmethod
    def __requireCredentials(self):

        __username = input(msg['login_username'])
        __password = getpass(prompt = msg['login_password'])

        query = db.read_where('Usuario','cpf',['=',__username])

        if (len(query) == 0):
            return(resultado(False,'Usuário inexistente'))
        else:
            if(spw.auth(query[list(query.keys())[0]]['senha'],'get') == __password):
                return(resultado(True,__username))
            else:
                return(resultado(False,'Senha incorreta'))
