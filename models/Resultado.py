class resultado:
            
            def __init__(self,resultado,mensagem,exception = None):
                self.resultado = resultado
                self.mensagem = mensagem
                self.exception = exception

            def get_resultado(self):
                return(self.resultado)

            def get_mensagem(self):
                return(self.mensagem)
