#Faça um programa que leia o nome e peso de várias pessoas
#guardando tudo em uma lista. No final, mostre:

#1. Quantas pessoas foram cadastradas.
#2. Uma listagem com as pessoas mais pesadas
#3. Uma listagem com as pessoas mais leves

'Definições'

people = list()
person = list()
weight = list()

'Adequando à proposta'

while True:

    print('-=' * 15)
    person.append(input('Nome: ').strip())
    person.append(float(input('Peso: ')))

    people.append(person[:])
    person.clear()

    user = None
    while user != 'S' and user != 'N':

        user = input('Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

for p in people:

    weight.append(p[1])
    weight.sort()

'Mostrando resposta'

print('-='*15)

#1. Quantas pessoas foram cadastradas.

print(f'Ao todo você cadastrou {len(people)} pessoas.')

#2. Uma listagem com as pessoas mais pesadas

print(f'O maior peso foi de {weight[-1]}kg por: ', end='')

for p in people:

    if p[1] == weight[-1]:

        print(f'{p[0]}... ', end='')

#3. Uma listagem com as pessoas mais leves

print(f'\nO menor peso foi de {weight[0]} por: ', end='')

for p in people:

    if p[1] == weight[0]:

        print(f'{p[0]}... ', end='')
