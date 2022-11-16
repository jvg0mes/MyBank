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
            self.user = auth.mensagem
        elif (auth.resultado == 'signin'):
            'registrar'
        else:
            print("\n" + auth.mensagem)
            raise(ValueError)

        class SessionKey():

            def __init__(self):
                
                r = SessionKey.generate_key()
                if r.resultado:
                    self.key = r.mensagem
                else:
                    raise(resultado(False,'Falha ao gerar a chave'))

            def generate_key():

                import random

                l = [chr(x) for x in range(97, 123)]
                lu = [chr(x).upper() for x in range(97, 123)]

                nk = random.randint(100000,999999)
                lk = random.choices(l,k=10)
                lku = random.choices(lu,k=5)
                rk = auth.mensagem.replace('.','').replace('-','')

                key = list(str(nk) + ''.join(lk) + ''.join(lku))
                random.shuffle(key)

                key = (''.join(key[0:3]) + rk[0:3] + ''.join(key[3:6]) +
                rk[3:6] + ''.join(key[6:9]) + rk[6:9] + 
                ''.join(key[9:12]) + rk[9:] + ''.join(key[12:]))

                # core = key[3:6] + key[9:12] + key[15:18] + key[21:23]

                return(resultado(True,key))

            def get_key(self):
                return(self.key)

        self.skey = SessionKey().get_key()

    @classmethod
    def __requireCredentials(self):

        __username = input(msg['login_username'])
        __password = getpass(prompt = msg['login_password'])

        if __username == 'signin':
            return(resultado(True,'signin'))

        query = db.read_where('Usuario','cpf',['=',__username])

        if (len(query) == 0):
            return(resultado(False,'Usuário inexistente'))
        else:
            if(spw.auth(query[list(query.keys())[0]]['senha'],'get') == __password):
                return(resultado(True,__username))
            else:
                return(resultado(False,'Senha incorreta'))
