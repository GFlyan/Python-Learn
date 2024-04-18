#Aprimore o desafio anterior, mostrando no final:

#1. A soma de todos os valores pares digitados.
#2. A soma dos valores de terceira coluna.
#3. O maior valor da segunda linha

'Defininções'

matrice = [[[], [], []], [[], [], []], [[], [], []]]
i = int()
j = int()
pair_sum = int()
sum_third_column = int()
mayor_second_line = list()

'Adequando à proposta'

print('-='*15)

for line in matrice:

    j = 0

    for column in line:

        line[j] = int(input(f'Digite um valor para [{i}, {j}]: '))

        j += 1

    i += 1

'Mostrando resultados'

print('-='*15)

for line in matrice:

    for column in line:

        print(f'[{column}]', end='')

        if (column % 2) == 0:

            pair_sum += column #1. A soma de todos os valores pares digitados.

    sum_third_column += line[2]
    print('\n', end='')

for column in matrice[1]:

    mayor_second_line.append(column)

print('-='*15)


#1.

print(f'A soma de todos os valores pares digitados: {pair_sum}')

#2.

print(f'A soma dos valores da terceira coluna: {sum_third_column}')

#3.

print(f'O maior valor da segunda linha: {sorted(mayor_second_line)[-1]}')