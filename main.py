import os
from msg.text import msg
from models.Cliente import Cliente
from models.Usuario import Usuario
from models.Login import Login
from services.database_service import database_service as dbs

nome= 'Joao'
idade='23'
cpf='123.123.123-12'
endereco = 'Avenida Central'
renda = 5000

state = True

clear = lambda : os.system('cls' if os.name=='nt' else 'clear')

print(Usuario('123-321-123.22','L@345679').registrar().mensagem)

print(dbs.read('Usuario'))

l = Login()