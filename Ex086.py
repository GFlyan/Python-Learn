#Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado

#No final mostre na tela com a formatação correta

matrice = [[[],[],[]], [[],[],[]], [[],[],[]]]
i = 0
j = 0

print('-'*30)

for line in matrice:

    j = 0

    for column in line:

        line[j] = int(input(f'Digite um valor para a entrada [{i},{j}]: '))
        
        j += 1

    i += 1

print(f'-='*15)

for line in matrice:

    for column in line:

        print(f'[{column:^3}]', end='')

    print()

print(f'-='*15)
