from abc import ABC, abstractmethod
from Projeto.modelos.endereco import Endereco

@abstractmethod
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str,salario: int, endereco: Endereco) -> None:
        self.nome     = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email    = self._verificar_email(email)
        self.salario  = self._verificar_salario(salario)
        self.endereco = endereco
        

    def _verificar_nome(self,valor):
        """Método para verificação de nome."""
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio_invalido(valor) 

        self.nome = valor
        return self.nome

    def _verificar_telefone(self,valor):
        """Método para verificação de telefone."""
        self._verificar_telefone_tipo_invalido(valor)
        self._verificar_telefone_vazio_invalido(valor)
        

        self.telefone = valor
        return self.telefone

    def _verificar_email(self,valor):
        """Método para verificação do e-mail."""
        self._verificar_email_tipo_invalido(valor)
        self._verificar_email_vazio_invalido(valor)

        self.email = valor
        return self.email
    

    def _verificar_salario(self,valor):
        '''Método para verificação do salario'''
        self._verificar_salario_vazio_invalido(valor)
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo_invalido(valor)
        

        self.salario = valor
        return self.salario
    
    # Métodos auxiliares.
  
    def _verificar_nome_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do nome do tipo invalido."""  
        if not isinstance (valor, str):
            raise TypeError ("O nome precisa ser uma sequência de texto.")
        
    def _verificar_nome_vazio_invalido(self,valor):
        """"Método auxiliar para verificação do nome do tipo vazio."""
        if not valor.strip():
            raise TypeError("O campo do nome não pode ser deixado em branco.")  

    def _verificar_telefone_tipo_invalido(self,valor):
        """"Método auxiliar para verificação do telefone do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError ("O campo do telefone não pode ser deixado em branco.")

    def _verificar_telefone_vazio_invalido(self,valor):
        """Método auxiliar para verifcação do telefone do tipo invalido."""
        if not valor.strip():
            raise TypeError ("O telefone precisa ser uma sequência de texto.")  
        
    def _verificar_email_tipo_invalido(self,valor):
        """Método auxuliar para verificação do e-mail do tipo invalido."""
        if not isinstance (valor, str):
            raise TypeError ("O e-mail precisa ser uma sequência de texto.")

    def _verificar_email_vazio_invalido(self,valor):
        """Método auxiliar para verificação do e-maiel do tipo."""
        if not valor.strip():
            raise TypeError ("O campo do e-mail não pode ser deixado em branco.")
    

    def _verificar_salario_vazio_invalido(self,valor):
        """Método para verificação do Salário vazio."""
        if valor is None:
            raise ValueError("O campo do salario não pode ser deixado em branco.")

    def _verificar_salario_tipo_invalido(self,valor):
        """Método para verificação do Salário invalido."""
        if not isinstance (valor, (int, float)):
            raise ValueError("O salario deve ser um numero.")
        
    def _verificar_salario_negativo_invalido(self, valor):
        """Método para verificar salário negativo.""" 
        if valor <= 0:
            raise ValueError ("O salario não pode ser negativo.")


    def __str__(self) -> str:
        return (            
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalário: R$ {self.salario} reais"  
            #f"\nSalário final: R$ {self.salario_final()} reais"
            f"\nEndereço: {self.endereco}"
            )