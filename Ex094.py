#Crie um programa que leia nome, sexo e idade de várias pessoas.
#Guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:

#1. Quantas pessoas foram cadastradas
#2. A media de idade do grupo
#3. Uma lista com todas as mulheres
#4. Uma lista com todas as pessoas com idade acima da média


'Definições'

people = list()
person = dict()

'Adequando à proposta'

while True:

    print('-='*15)

    person['Nome'] = input('Nome: ').strip().capitalize()
    person['Sexo'] = input('Sexo: [M/F] ').upper()
    person['Idade'] = int(input('Idade: '))
    people.append(person.copy()) 
        
    user = None

    while user != 'S' and user != 'N':

        user = input('Quer continuar? [S/N] ').upper()

    if user == 'N': 

        break

'Mostrando resultados'

print('-='*15)

#1. Quantas pessoas foram cadastradas

print(f'-O grupo tem {len(people)} {"pessoas" if len(people) != 1 else "pessoa"}.')

#2. A media de idade do grupo

ages = int()
for p in people:

    ages += p['Idade']

print(f'-A média de idade é de {ages/len(people)} anos.')

#3. Uma lista com todas as mulheres

print('-As mulheres cadastradas foram: ', end='')

for p in people:

    if p['Sexo'] == 'F':

        print(p['Nome'], end=' ')
    
#4. Uma lista com todas as pessoas com idade acima da média
print()
print('\nLista das pessoas que estão acima da média: ')

for p in people:

    if p['Idade'] > ages/len(people):

        print('-'*30)
        print(f'Nome: {p["Nome"]}\nSexo: {p["Sexo"]}\nIdade: {p["Idade"]}')