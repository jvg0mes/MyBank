import pytest
from ..models.Cliente import Cliente

class TestModelsClass:
    
    nome = "Joao"
    idade = 23
    cpf = "123.456.789-12"
    endereco = "Avenida Amacieiras"
    renda = 1000
    
    def test_criacao_cliente_valido(self):
        
        #given
        
        #when
        cliente = Cliente(self.__class__.nome,self.__class__.idade,self.__class__.cpf,self.__class__.endereco,self.__class__.renda)
        
        #then
        
        assert((cliente.nome == self.nome) &
               (cliente.idade == self.idade) &
               (cliente.cpf == self.cpf) &
               (cliente.endereco == self.endereco) &
               (cliente.renda == self.renda))
    
    #######
    # Validacoes CPF
    #######
    
    def test_tentativa_criacao_cliente_com_cpf_invalido_tamanho(self):
        
        with pytest.raises(ValueError):
            
            # given
            cpf = "123.456.789-1"
            
            # when
            cliente = Cliente(self.__class__.nome,self.__class__.idade,cpf,self.__class__.endereco,self.__class__.renda)
            
            # then
            assert cliente
            
    def test_tentativa_criacao_cliente_com_cpf_invalido_formato(self):
        
        with pytest.raises(ValueError):
            
            # given
            cpf = "b23.456.789-1a"
            
            # when
            cliente = Cliente(self.__class__.nome,self.__class__.idade,cpf,self.__class__.endereco,self.__class__.renda)
            
            # then
            assert cliente
    
    def test_tentativa_criacao_cliente_com_cpf_invalido_caracteres_especiais(self):
        
        with pytest.raises(ValueError):
            
            # given
            cpf = "123-456.789-12"
            
            # when
            cliente = Cliente(self.__class__.nome,self.__class__.idade,cpf,self.__class__.endereco,self.__class__.renda)
            
            # then
            assert cliente
        