#Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
#aleatórios.

#Guarde esses resultados em um dicionário. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número do dado

'Definições'

from time import sleep
from random import randint
from operator import itemgetter

players = list()
person = dict()

'Adequando à proposta'

print('Valores sorteados:')

for c in range (4):
    
    person[f'Jogador {c+1}'] = randint(1, 6)

players.append(person.copy())

for i in players:

    for k, v in i.items():
 
        sleep(1)
        print(f'O {k} tirou {v}')


print('-='*15)
print(f'Ranking dos jogadores:')

players = sorted(person.items(), key=itemgetter(1), reverse=True)

for c, p in enumerate(players):

    print(f'{c+1}º lugar: {p[0]} com {p[1]}')