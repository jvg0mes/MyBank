import os
import shelve
from base64 import encode,decode
from getpass import getpass
from msg.text import msg
from models.Cliente import Cliente
from models.Conta import Conta
from models.Transacao import Transacao

state = True

clear = lambda : os.system('cls' if os.name=='nt' else 'clear')

class Login():

    def __init__(self):
        print(msg['login_main'])
        self.requireUsername()
        self.requirePassword()

    def requireUsername(self):
        self.__username = input(msg['login_username'])

    def requirePassword(self):
        self.__password = getpass(prompt = msg['login_password'])

mylogin = Login()

# credentials = shelve.open('./mocks/credentials')

# credentials.insert({'username:'})