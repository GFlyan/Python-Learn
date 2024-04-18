#Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'Definições'

group = list()
person = list()

'Adequando à proposta'

while True:

    person.append(input('Nome: '))
    person.append(int(input('Nota 1: ')))
    person.append(int(input('Nota 1: ')))

    group.append(person[:])
    person.clear()

    user = None
    while user != 'S' and user != 'N':

        user = input('Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break