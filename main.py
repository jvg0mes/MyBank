from models.Cliente import Cliente
from models.Conta import Conta
from models.Transacao import Transacao

nome = "Joao"
idade = 23
cpf = "123.456.789-12"
endereco = "Avenida Amacieiras"
renda = 1000

cliente = Cliente(nome,idade,cpf,endereco,renda)

senha_correta = '$Joao123'
senha_invalida_max_caracteres = '$Joao1234'
senha_invalida_sem_caracter_especial = 'iJoao123'
senha_invalida_sem_caracter_maiusculo = '*joao123'

print("Ola")

conta = Conta(cliente,senha_correta)