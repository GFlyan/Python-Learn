#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares e
#ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'Definições'

values = [[], []]

'Adequando à proposta'

for c in range(0, 7):

    value = int(input(f'Digite o {c+1}° valor: '))

    if (value % 2) == 0:

        values[0].append(value)

    else:

        values[1].append(value)

'Mostrando resposta'

print('-='*15)

#Valores pares

print(f'Os valores pares digitados foram: {sorted(values[0])}')

#Valores ímpares

print(f'Os valores ímpares digitados foram: {sorted(values[1])}')
