import shelve
from models.Resultado import resultado

class database_service():

    def open_connection(table):

        path = "./mocks/"

        return(shelve.open(path + table))

    def check_schema(obj,table):

        from .schema import schemas

        print("-"*50 + 'schemas' + "-"*50 + "\n")
        print(schemas)
        print("\n" + "-"*100 + "\n")

        if type(obj) == schemas[table]:
            return(resultado(True,'Schema valido'))
        else:
            return(resultado(False,'Schema invalido'))

    def get_id(table):

        dbase = database_service.open_connection('dbase')

        return(dbase[table])


    def write(obj,table : str, replace = False):

        # valida se a primeira key é o nome da tabela

            scheck = database_service.check_schema(obj = obj,table = table)

            print(scheck.resultado)

            if scheck.resultado == True:

                row_id = database_service.get_id(table)

                if ((replace == False) & (type(replace) == bool)):
                    data = {str(row_id):obj.__dict__}
                else:
                    data = {str(replace):obj.__dict__}

                with database_service.open_connection(table) as db:          

                    db.update(data)
                    db.close()

                with database_service.open_connection('dbase') as dbase:          

                    dbase.update({table : (row_id + 1)})
                    dbase.close()

            
                return(resultado(True,"Operacao realizada com sucesso"))

            else:

                return(resultado(False,scheck.mensagem))

    def read(table : str):

        db = database_service.open_connection(table)

        elist = {}

        for k,v in db.items():
            elist.update({k:v})

        return(elist)

    def read_column(table : str,column : str):

        db = database_service.open_connection(table=table)
        
        elist = {}

        for k,v in db.items():
            elist.update({k:v[column]})

        return(elist)

    def read_line(table,key):

        db = database_service.open_connection(table=table)

        return({key:db[key]})

    def read_where(table : str,
                   column : str,condition : list):

        db = database_service.open_connection(table=table)

        op = condition[0]

        def evaluate(x,base):
            if (op == '=') | (op == '=='):
                return(x == base)
            elif (op == '!=') | (op == '<>'):
                return(x != base)
            elif op == '>':
                return(x > base)
            elif op == '<':
                return(x < base)
            elif op == '>=':
                return(x >= base)
            elif op == '<=':
                return(x <= base)
            elif op == 'in':
                return(x in base)
            elif op == 'not in':
                return(x not in base)
            else:
                raise(Exception)
            
        elist = {}

        for k,v in db.items():
            if evaluate(v[column],condition[1]):
                elist.update({k:v})

        return(elist)

# dbs = database_service()

# c = Cliente('joao noah victor',1,'231.213.123-28','nenhum',6000)

# dbs.write(obj = c, table = 'Cliente')

# dbs.read('Cliente')
# dbs.read_column('Cliente','cpf')
# dbs.read_line('Cliente','1')
# dbs.read_where('Cliente','nome',['==','mattia'])
# dbs.read_where('Cliente','renda',['>',5500])
# dbs.read_where('Cliente','renda',['>',8000])