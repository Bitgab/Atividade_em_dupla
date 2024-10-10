import pytest
from modelos.funcionario import Funcionario
from modelos.endereco                import Endereco
from modelos.enums.unidadeFederativa import UnidadeFederativa
from modelos.enums.sexo import Sexo

# Boas práticas de progamação.
@pytest.fixture

def funcionario_valida():
    funcionario = Funcionario("Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA))
    return funcionario

def test_nome_valido(funcionario_valida):
    assert funcionario_valida.nome == "Fuboca"

def test_telefone(funcionario_valida):    
    assert funcionario_valida.telefone == "71912345678"

def test_email(funcionario_valida):
    assert funcionario_valida.email == "fuboca@gmail.com"

def test_nome_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O nome precisa ser uma sequência de texto."):
        Funcionario(12,"71912345678","fuboca@gmail.com",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA))

def test_nome_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do nome não pode ser deixado em branco."):
        Funcionario("71912345678","fuboca@gmail.com",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA))  

def test_telefone_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do telefone não pode ser deixado em branco."):
        Funcionario("Fuboca",12,"fuboca@gmail.com",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA)) 

def test_telefone_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O telefone precisa ser uma sequência de texto."):
        Funcionario("Fuboca","","fuboca@gmail.com",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA)) 
def test_telefone_tamanho_invalido_retornar_mensagem_de_erro():
    with pytest.raises(ValueError, match="O telefone deve ter exatamente 11 caracteres."):
        Funcionario("Fuuboca", "123456789", "fuboca@gmail.com", Endereco("Rua A", "1234", " Perto da padaria do seu zé", "123456789", "Salvador", UnidadeFederativa.BAHIA))
        
def test_email_tipo_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O e-mail precisa ser uma sequência de texto."):
        Funcionario("Fuboca","71912345678",12,Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA))

def test_email_vazio_invalido_retornar_mensagem_de_erro():
    with pytest.raises(TypeError, match = "O campo do e-mail não pode ser deixado em branco."):
        Funcionario("Fuboca", "71912345678","",Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA))