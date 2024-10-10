from Projeto.modelos.funcionario        import Funcionario
from Projeto.modelos.endereco           import Endereco


class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, salario, endereco, crea: str):
       super().__init__(nome, telefone, email, salario, endereco)
       self.crea = self._verificar_crea(crea)
    
    # Métodos de verificar
    def _verificar_crea(self,valor):
        '''Método para verificação do CREA'''
        self._verificar_crea_tipo_invalido_retorna_erro(valor)
        self._verificar_crea_vazio_invalido_retorna_erro(valor)

        self.crea = valor
        return self.crea
    

    def _verificar_crea_tipo_invalido_retorna_erro(self,valor):
        """Método para verificação do CREA invalido"""
        if not isinstance (valor,str):
            raise TypeError('O CREA deve ser um texto.')

    def _verificar_crea_vazio_invalido_retorna_erro(self,valor):
         """Método para verificação do CREA vazio"""
         if not valor.strip(): 
            raise TypeError('O CREA não pode estar vazio.')

    