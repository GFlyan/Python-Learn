#Aprimore o desafio anterior, mostrando no final.

#1. A soma de todos os valores pares digitados.
#2. A soma dos valores da terceira coluna.
#3. O maior valor da segunda linha.

matrice = [[[],[],[]], [[],[],[]], [[],[],[]]]
i = 0
j = 0
pairs = int()
sum_third_column = int()
mayor_second_line = list()

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

        if (column % 2) == 0: #1. A soma de todos os valores pares digitados.
        
            pairs += column

        print(f'[{column:^3}]', end='')

    sum_third_column += line[2] #2. A soma dos valores da terceira coluna.

    print('\n', end='')

for v in matrice[1]:

    mayor_second_line.append(v) #3. O maior valor da segunda linha.

print(f'-='*15)

#1. A soma de todos os valores pares digitados.
print(f'A soma de todos os valores pares digitados é: {pairs}')
#2. A soma dos valores da terceira coluna.
print(f'A soma dos valores da terceira coluna é: {sum_third_column}')
#3. O maior valor da segunda linha.
print(f'O maior valor da segunda linha é: {sorted(mayor_second_line)[-1]}')