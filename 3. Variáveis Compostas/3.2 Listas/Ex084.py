#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
#No final mostre:

#1.Quantas pessoas foram cadastradas
#2.Uma listagem com as pessoas mais pesadas
#3.Uma listagem com as pessoas mais leves

'Definições'

people = list()
person = list()
weight = list()

'Adequando à Proposta'

while True:

    print('-='*15)
    person.append(input('Nome: '))
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

'Mostrando Resultados'

print('-='*15)
#1.
print(f'{len(people)} {"pessoas foram cadastradas" if len(people) != 1 else "pessoa foi cadastrada"}')

#2.
print(f'O maior peso obtido foi {weight[-1]}kg, por: ', end='')
for p in people:

    if p[1] == weight[-1]:

        print(f'{p[0]}... ', end='')

#3.    
print(f'\nO menor peso obtido foi {weight[0]}kg, por: ', end='')
for p in people:

    if p[1] == weight[0]:

        print(f'{p[0]}... ', end='')
