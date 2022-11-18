from .Resultado import resultado

class Cliente:
    
    def __init__(self, nome : str , idade : int, 
                 cpf : str, endereco : str, 
                 renda: float, idCliente : int):
        
        self.nome = nome
        self.idade = idade
        
        validacao_cpf = Cliente.valida_cpf(cpf)
        if (validacao_cpf.resultado):
            self.cpf = cpf
        else:
            raise ValueError(validacao_cpf.mensagem)
        
        self.endereco = endereco
        self.renda = renda
        self.idCliente = idCliente
    
    def valida_cpf(cpf : str):
        
        numbers = range(0,10)
        numbers_str = [str(x) for x in numbers]
        
        def _verifica_trechos_numericos(lista_de_trechos):
            
            def _verifica_trecho_numerico(trecho):
                if((sum([x in numbers_str for x in trecho])/len(trecho)) == 1):
                    return True
                else:
                    return False
            
            if (sum([_verifica_trecho_numerico(trecho_numerico) for trecho_numerico in lista_de_trechos])/
            len(lista_de_trechos)) == 1:
                return True
            else:
                return False
            
        def _verifica_caracteres_especiais(lista_de_caracteres_especiais):
            
            validacoes =  (
                (lista_de_caracteres_especiais[0] == '.') &
                (lista_de_caracteres_especiais[1] == '.') &
                (lista_de_caracteres_especiais[2] == '-')
            )
            
            if (validacoes):
                return True
            else:
                return False
            
        if len(cpf) != 14:
            return resultado(False,"Tamanho invalido de CPF")
        else:
            trechos_numericos = [cpf[0:3],cpf[4:7],cpf[8:11],cpf[12:]]
            caracteres_especiais = [cpf[3],cpf[7],cpf[11]]        
            
        if( _verifica_trechos_numericos(trechos_numericos) &
            _verifica_caracteres_especiais(caracteres_especiais)):
            return resultado(True,"CPF valido")
        else:
            return resultado(False,"Formato incorreto de CPF")
