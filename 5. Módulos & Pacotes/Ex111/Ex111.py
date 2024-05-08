#Crie um pacote chamado utilidadesCeV que tenha um módulo interno chamado moeda.

#Transfira todas as funções utilizadas nos Ex's 107, 108, 109 e 110 para o módulo e mantenha tudo funcionando.

from Package import moeda

value = float(input('Digite o preço: R$'))
increase = int(input('Quantos porcento deseja aumentar: '))
depreciate = int(input('Quantos porcento deseja diminuir: '))
moeda.resumo(value=value, increase=increase, depreciate=depreciate)