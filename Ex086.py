#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
#lidos pelo teclado.

#No final mostre a matriz na tela com a formação correta.

'Defininções'

matrice = [[[], [], []], [[], [], []], [[], [], []]]
i = int()
j = int()

'Adequando à proposta'

for line in matrice:

    for column in line:

        column.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        j += 1

    i += 1

'Mostrando resultados'

print('-='*15)

for line in matrice:

    for column in line:

        print(f'{column}', end='')

    print('\n', end='')
