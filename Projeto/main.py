import os 
import sys
os.system("cls || clear")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Projeto.modelos.engenheiro import Engenheiro
from Projeto.modelos.funcionario import Funcionario
from Projeto.modelos.endereco import Endereco
from Projeto.modelos.medico import Medico
from Projeto.modelos.enums.unidadeFederativa import UnidadeFederativa
from Projeto.modelos.enums.sexo import Sexo

funcionario = Funcionario("Fuboca","71912345678","fuboca@gmail.com",Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO,"25/10/2005","123.456.789-00","12.345.567-89","021024",10000)
medico = Medico('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',1000,'017')
engenheiro = Engenheiro('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),Sexo.MASCULINO,'25/10/2005',"956.745.558-78",'15.457.598-74','0101',1000,'017')


# Inicia o test no terminal
if __name__ == '__main__':
    os.system('pytest ')

print(funcionario)