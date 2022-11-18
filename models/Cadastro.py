from models.Usuario import Usuario
from services.database_service import database_service as dbs
from .Cliente import Cliente
from msg.text import msg
from .Resultado import resultado
from sec.spw import spw

class Cadastro():

    debug = False

    def __init__(self):
        pass
 
    def cadastrar(self):

        r1 = self.cadastrar_cliente()

        if r1.get_resultado() == False:
            return(resultado(False,'Falha ao cadastrar o cliente'))

        r2 = False
        r2_msg = 'Inicio'
        while ((r2 == False) & 
        (r2_msg in ['Senha de confirmacao divergente\n','Inicio'])):
            obj = self.criar_usuario()
            r2 = obj.get_resultado()
            r2_msg = obj.get_mensagem()

        return(resultado(True,'Cadastro realizado com sucesso'))

    def cadastrar_cliente(self):

        arg_list = []

        print(msg['cadastrar_cliente'])

        for l in msg['cadastrar_cliente_campos']:

            valid =  l != '\nidCliente: '
            
            if valid:
                v = input(l)
            else:
                v = l

            if Cadastro.debug: print(f'l={l}',f'\nv={v}')

            if l[0:3] == 'cpf':
                if len(dbs.read_where('Cliente',
                        'cpf',['==',v])) > 0:
                    if Cadastro.debug: print('CLIENTE JA CADASTRADO')
                    return(resultado(False,'Cliente ja cadastrado'))

            from services.database_service import database_service as db
    
            if not valid:
                arg_list.append(dbs.get_id('Cliente'))
            else:
                arg_list.append(v)

        from sec.spw import spw

        try:
            
            dbs.write(Cliente(*arg_list),'Cliente',False)
            if Cadastro.debug: print("CLIENTE ESCRITO NO BANCO COM SUCESSO")

            self.cliente = Cliente(*arg_list)

            return(resultado(True,"Cliente cadastrado com sucesso"))

        except Exception as e:
            return resultado(False,'Falha ao cadastrar o cliente')




    def criar_usuario(self):

        username = self.cliente.cpf

        if Cadastro.debug: print(username)

        if len(dbs.read_where('Cliente','cpf',['==',username]))<1:
            if Cadastro.debug: print('CLIENTE NAO ENCONTRADO')
            return(resultado(False,'Cliente nao encontrado'))

        if len(dbs.read_where('Usuario','cpf',['==',username]))>0:
            if Cadastro.debug: print('USUARIO JA EXISTE')
            return(False,'Usuario ja existe')

        senha = input(msg['cadastrar_usuario_senha'][0])
        csenha = input(msg['cadastrar_usuario_senha'][1])        

        if (senha != csenha):
            return(resultado(False,'Senha de confirmacao divergente\n'))

        idCliente = dbs.read_where('Cliente','cpf',
                                  ['==',username])

        if len(idCliente) == 0:
            if Cadastro.debug: print('idCLIENTE NAO ENCONTRADO')
            return(resultado(False,'Cliente nao encontrado'))
        else:
            print(idCliente)
            idCliente = idCliente[list(idCliente.keys())[0]]['idCliente']

        idUsuario = dbs.get_id('Usuario')

        dbs.write(Usuario(username,spw.auth(senha,"set"),
                  idCliente,idUsuario),
                 'Usuario',False)
        if Cadastro.debug: print("USUARIO ESCRITO NO BANCO COM SUCESSO")

        return(resultado(True,'Usuario criado com sucesso'))

