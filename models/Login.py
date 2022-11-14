from msg.text import msg
from getpass import getpass
import shelve
from sec.spw import spw
from .Resultado import resultado

tablepath = "./mocks/credentials"

db= shelve.open(tablepath)

db.update({'joao':spw.auth('12345',"set")})

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

        db = shelve.open(tablepath)

        __username = input(msg['login_username'])
        __password = getpass(prompt = msg['login_password'])

        if (__username not in db.keys()):
            db.close()
            return(resultado(False,'Usuário inexistente'))
        else:
            if(spw.auth(db[__username],'get') == __password):
                db.close()
                return(resultado(True,__username))
            else:
                db.close()
                return(resultado(False,'Senha incorreta'))
