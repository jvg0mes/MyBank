import os
import shelve
from base64 import encode,decode
from msg.text import msg
from models.Cliente import Cliente
from models.Conta import Conta
from models.Transacao import Transacao
from models.Login import Login

state = True

clear = lambda : os.system('cls' if os.name=='nt' else 'clear')

mylogin = Login()
