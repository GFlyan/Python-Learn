#Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
#aleatórios.

#Guarde esses resultados em um dicionário. No final, coloque esse dicionário
#em ordem, sabendo que o vencedor tirou o maior número do dado

'Definições'

from random import randint
person = dict()
values = list()
winner = list()

'Adequando à proposta'

for c in range (4):

    person[f'Jogador {c+1}'] = randint(1, 6)


for v in person.values():

    values.append(v)
    values.sort()

for k, v in person.items():

    if v == values[-1]:

        winner.append(k)

print(f'O maior valor foi {values[-1]}, e o ganhador foi o {winner}')