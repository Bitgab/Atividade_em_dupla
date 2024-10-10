import pytest
from Projeto.modelos.medico import Medico
from Projeto.modelos.endereco import Endereco
from Projeto.modelos.enums.unidadeFederativa import UnidadeFederativa
from Projeto.modelos.enums.sexo import Sexo

# Boas práticas de progamação.
@pytest.fixture
def medico_valido():
    medico = Medico("Fuboca","7191234-5678","fuboca@gmail.com",1000,Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA),"1234")
    return medico

def test_verificar_crm_tipo_invalido_retorna_erro(medico_valido):
    assert medico_valido.crm == '1234'

def test_verificar_crm_tipo_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O crm deve ser um texto.'):
        Medico("Fuboca","7191234-5678","fuboca@gmail.com",1000,Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA),1234)      
def test_verificar_crm_vazio_invalido_retorna_erro():
    with pytest.raises(TypeError,match = 'O crm não pode estar vazio.'):
        Medico("Fuboca","7191234-5678","fuboca@gmail.com",1000,Endereco("Rua A", "12"," Perto da padaria do seu zé","12345","Salvador",UnidadeFederativa.BAHIA),"")