#Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
#aleatórios.

#Guarde esses resultados em um dicionário. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número do dado

'Definições'

from time import sleep
from random import randint
players = list()
person = dict()

'Adequando à proposta'

print('Valores sorteados:')

for c in range (4):
    
    person[f'Jogador {c+1}'] = randint(1, 6)
    players.append(person.copy())
    person.clear()

for i in players:

    for k, v in i.items():
 
        sleep(1)
        print(f'O {k} tirou {v}')


print('-='*15)
print(f'Ranking dos jogadores:')


