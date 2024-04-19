#Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
#aleatórios.

#Guarde esses resultados em um dicionário. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número do dado

'Definições'

from time import sleep
from random import randint
payers = list()
person = dict()

'Adequando à proposta'

for c in range (4):

    sleep(1)
    person[f'Jogador {c+1}'] = randint(1, 6)

for k, v in person.items():

    print(f'O {k} tirou {v}')


print('-='*15)
print(f'Ranking dos jogadores:')

