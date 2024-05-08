#Crie um programa que vai ler vários números e colocar em uma lista.

#Depois disso, crie duas listas extras que vão conter apenas os valores
#pares e os valores impares digitados, respectivamente.

#Ao final mostre o conteúdo das três listas geradas.

'Definições'

values = []

'Adequando à proposta'

while True:

    while True:

        value = int(input('Digite um número: '))

        if value in values:

            print('Valor duplicado! Insira outro número.')

        else:

            values.append(value)
            break

    user = input('Quer continuar? [S/N] ').strip().upper()

    while user != 'S'and user != 'N':

        user = input('Não entendi... Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

#Listas Par/Ímpar

pair_values = []
odd_values = []

for v in values:

    if (v % 2) == 0:

        pair_values.append(v)

    else:

        odd_values.append(v)

'Produto final'
print('-='*20)
print(f'A lista completa é: {values}')
print(f'A lista de pares é: {pair_values}')
print(f'A lista de impares é: {odd_values}')



