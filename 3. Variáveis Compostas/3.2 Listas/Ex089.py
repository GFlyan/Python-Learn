#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'Definições'

group = list()
person = list()

'Adequando à proposta'

while True:
        
    person.append(input('Nome: ').title()) #Name
    person.append(float(input('Nota 1: '))) #First
    person.append(float(input('Nota 2: '))) #Second

    group.append(person[:])
    person.clear()

    user = None
    while user != 'S' and user != 'N':

        user =  input('Quer continuar? [S/N] ').strip().upper()

    print('-='*15)

    if user == 'N':

        break

'Mostrando resultados'

print(f'Nº   {"NOME":<15}MÉDIA')
print('-'*30)

for c, p in enumerate(group):

    print(f'{c}    {p[0]:<15}{(p[1]+p[2])/2}')

print('-'*30)

while True:

    while True:

        show = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
        
        if show  <= len(group)-1 or show == 999:

            break

        else:

            print('Não entendi...', end=' ')
    
    if show == 999:
    
        break
    
    print(f'Notas de {group[show][0]} são: {group[show][1:]}')

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')