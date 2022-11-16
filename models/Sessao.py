from .Login import Login
from .Resultado import resultado
from services.database_service import database_service as dbs
import atexit
from datetime import datetime as dt

class Sessao():

    def __init__(self,login : Login):
        
        self.session_id = login.skey
        self.user = login.user
        self.status = True
        self.data_inicio = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data_fim = None
    
        dbs.write(self,'Sessao')
        atexit.register(self.finalizar)
        
    def finalizar(self):

        self.status = False
        self.data_fim = dt.now().strftime('%Y-%m-%d %H:%M:%S')

        condition = dbs.read_where('Sessao','session_id',['=',self.session_id])

        dbs.write(self,'Sessao',replace = list(condition.keys())[0])

        return(resultado(True,'Sessao finalizada'))
