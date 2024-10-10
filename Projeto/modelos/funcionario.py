from modelos.endereco import Endereco
from modelos.enums.unidadeFederativa import UnidadeFederativa
from modelos.enums.sexo import Sexo

class Funcionario:
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome     = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email    = self._verificar_email(email)
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
        self._verificar_telefone_tamanho_invalido(valor)

        self.telefone = valor
        return self.telefone

    def _verificar_email(self,valor):
        """Método para verificação do e-mail."""
        self._verificar_email_tipo_invalido(valor)
        self._verificar_email_vazio_invalido(valor)

        self.email = valor
        return self.email