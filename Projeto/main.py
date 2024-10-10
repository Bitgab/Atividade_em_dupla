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

import os 
import sys
os.system("cls || clear")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Projeto.modelos.engenheiro import Engenheiro
from Projeto.modelos.funcionario import Funcionario
from Projeto.modelos.endereco import Endereco
from Projeto.modelos.medico import Medico
from Projeto.modelos.enums.unidadeFederativa import UnidadeFederativa


funcionario = Funcionario("Fuboca","71912345678","fuboca@gmail.com",1000,Endereco("Rua A","12","Perto","1234567","Salvador",UnidadeFederativa.BAHIA))
medico = Medico('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',1000,Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),'017')
engenheiro = Engenheiro('Gabriel Fuboca','71555-9555','gabriel.fuboca@gmail.com',1000,Endereco('Rua A', '33','logo ali', '45658-565','salvador',UnidadeFederativa.SAO_PAULO),'017')


# Inicia o test no terminal
if __name__ == '__main__':
    os.system('pytest ')

print(funcionario)