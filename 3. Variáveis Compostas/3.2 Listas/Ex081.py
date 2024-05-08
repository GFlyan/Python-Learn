#Crie um programa que vai ler vários números e colocar em uma lista

#Depois disso mostre:


#1. Quantos números foram digitados
#2. A lista de valores, ordenada de forma decrescente
#3. Se o valor 5 foi digitado e está ou não na lista'Definições'

'Definições'

values = []

'Adequando à proposta'

while True:

    while True:

        value = int(input('Digite um valor: '))

        if value in values:

            print('Valor duplicado! Insira outro número.')

        else:

            values.append(value)
            break

    user = input('Quer continuar? [S/N] ').strip().upper()
    while user != 'S' and user != 'N':

        user = input('Não entendi... Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

'Produto final'

print('-='*20)

#1. Quantos números foram digitados

print(f'Foram digitados {len(values)} valores!')

#2. A lista de valores, ordenada de forma decrescente

print(f'A lista ordenada de forma decrescene fica: {sorted(values, reverse=True)}')

#3. Se o valor 5 foi digitado e está ou não na lista

if 5 in values:

    print(f'O valor 5 foi digitado e está na posição: {values.index(5)}')

else:

    print('O valor 5 não foi digitado!')