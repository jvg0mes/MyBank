import pytest
from ..models.Conta import Conta
from ..models.Cliente import Cliente

class TestModelsClassConta:
    
    
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
    senha_invalida_sem_caracter_numerico = '*joaovpy'
    
    def test_criacao_conta_valida(self):
        
        conta = Conta(self.__class__.cliente,
        self.__class__.senha_correta)
        
        assert((conta.senha == self.__class__.senha_correta)
            )
    
    def test_criacao_conta_invalida_maximo_caracteres(self):
        
        with pytest.raises(ValueError):
        
            #given
            
            #when
            
            result = Conta(self.__class__.cliente,
                self.__class__.senha_invalida_max_caracteres)
            
            #then
            assert(result)
    
    def test_criacao_conta_invalida_sem_caracter_especial(self):
        
        with pytest.raises(ValueError):
        
            #given
            
            #when
            
            result = Conta(self.__class__.cliente,
                self.__class__.senha_invalida_sem_caracter_especial)
            
            #then
            assert(result)
        
    def test_criacao_conta_invalida_sem_caracter_maiusculo(self):
        
        with pytest.raises(ValueError):
        
            #given
            
            #when
            
            result = Conta(self.__class__.cliente,
                self.__class__.senha_invalida_sem_caracter_maiusculo)
            
            #then
            assert(result)

    def test_criacao_conta_invalida_sem_caracter_numerico(self):
        
        with pytest.raises(ValueError):
        
            #given
            
            #when
            
            result = Conta(self.__class__.cliente,
                self.__class__.senha_invalida_sem_caracter_numerico)
            
            #then
            assert(result)    