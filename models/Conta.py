from .Cliente import Cliente
from .Resultado import resultado

class Conta(Cliente):
    
    def __init__(self, cliente: Cliente,senha: str):
        
        self.cpf = cliente.cpf
        
        validacao_senha = Conta.valida_senha(senha)
        if validacao_senha.resultado:
            self.senha = senha
        else:
            raise(ValueError(validacao_senha.mensagem))
        
    def valida_senha(senha : str):
        
        numbers = range(0,10)
        numbers_str = [str(x) for x in numbers]
        caracteres_especiais = '@#$%¨&*()-=\/?:.,^~;`´[]{\}//|'
        caracteres_maiusculos = 'QWERTYUIOPASDFGHJKLZXCVBNM'

        def _verifica_trecho_numerico(trecho):
            if((sum([x in numbers_str for x in trecho])) > 0):
                return True
            else:
                return False
            
        def _verifica_caracteres_especiais(trecho):
            if((sum([x in caracteres_especiais for x in trecho])) > 0):
                return True
            else:
                return False

        def _verifica_caracteres_maiusculos(trecho):
            if((sum([x in caracteres_maiusculos for x in trecho])) > 0):
                return True
            else:
                return False
            
        if len(senha) != 8:
            return resultado(False,"Tamanho invalido de Senha")   
            
        if( _verifica_trecho_numerico(senha) &
            _verifica_caracteres_especiais(senha) &
            _verifica_caracteres_maiusculos(senha)):
            return resultado(True,"Senha valido")
        else:
            return resultado(False,"Formato incorreto de Senha")