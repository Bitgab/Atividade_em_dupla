from Projeto.modelos.funcionario        import Funcionario
from Projeto.modelos.endereco           import Endereco
from Projeto.modelos.enums.sexo         import Sexo

class Medico(Funcionario):
    def __init__(self,nome:str,telefone:str,email:str,
                 endereco: Endereco,
                 sexo: Sexo ,
                 dataNascimento: str ,cpf:str,rg:str,matricula:str,salario:float,crm:str) -> None:
        super().__init__(nome ,telefone ,email ,endereco ,sexo ,dataNascimento,cpf,rg,matricula,salario)
        self.crm = self._verificar_crm(crm)
    
    # Métodos de verificar
    def _verificar_crm(self,valor):
        '''Método para verificação do crm'''
        self._verificar_crm_tipo_invalido_retorna_erro(valor)
        self._verificar_crm_vazio_invalido_retorna_erro(valor)

        self.crm = valor
        return self.crm
    

    def _verificar_crm_tipo_invalido_retorna_erro(self,valor):
        """Método para verificação do crm invalido"""
        if not isinstance (valor,str):
            raise TypeError('O crm deve ser um texto.')

    def _verificar_crm_vazio_invalido_retorna_erro(self,valor):
         """Método para verificação do crm vazio"""
         if not valor.strip(): 
            raise TypeError('O crm não pode estar vazio.')

    