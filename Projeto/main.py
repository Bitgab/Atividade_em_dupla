    # =========================== #
    #        Samir Santos         #
    #                             #
    #        Gabrel Bittecurt     #
    #                             #
    #        Turma 91210          #
    #                             #
    #        Senai || Fieb        #
    #                             #
    #        Salvador/BA          #
    # =========================== #
#python -m Projeto.main
import os 
import sys
os.system("cls || clear")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelos.enums.unidadeFederativa import UnidadeFederativa
from modelos.endereco import Endereco
from modelos.funcionario import Funcionario
from modelos.engenheiro import Engenheiro
from modelos.medico import Medico



funcionario = Funcionario("Fuboca","71912345678","fuboca@gmail.com",1000,Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA))
medico = Medico('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',1000,Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),'017')
engenheiro = Engenheiro('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',1000,Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),'017')


# Inicia o test no terminal
if __name__ == '__main__':
    os.system('pytest ')

print(engenheiro)