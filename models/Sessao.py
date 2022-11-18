from .Login import Login
from .Resultado import resultado
from .Cliente import Cliente
from .Usuario import Usuario
from services.database_service import database_service as dbs
import atexit
from datetime import datetime as dt

class Sessao():

    debug = True

    def __init__(self,login : Login):
        
        self.session_id = login.skey
        self.user = login.user
        self.status = True
        self.data_inicio = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data_fim = None
    
        dbs.write(self,'Sessao')

        self.catch_infos()

        atexit.register(self.finalizar)
        
    def finalizar(self):

        self.status = False
        self.data_fim = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        
        del self.infos

        condition = dbs.read_where('Sessao','session_id',['=',self.session_id])

        dbs.write(self,'Sessao',replace = list(condition.keys())[0])

        return(resultado(True,'Sessao finalizada'))

    def refresh(self):
        pass

    def catch_infos(self):
        
        def get_values(x):
            return x[list(x.keys())[0]]

        def get_column(c,x):
            return get_values(x)[c]
        
        cliente = Cliente(**get_values(dbs.read_where('Cliente',
                                  'cpf',['==',self.user])))
        if Sessao.debug: print('Cliente capturado pela sessao')

        usuario = Usuario(**get_values(dbs.read_where('Usuario',
                            'idCliente',['==',cliente.idCliente])))
        if Sessao.debug: print('Usuario capturado pela sessao')

                       
        self.infos = {'Cliente':cliente,'Usuario':usuario}

        if Sessao.debug: print('INFORMACOES DA SESSAO CAPTURADAS')         
