#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:

#1. Quantas vezes apareceu o valor 9
#2. Em que posição foi digitado o primeiro valor 3
#3. Quais foram os números pares.

'Definições'

v1 = int(input('Digite o primeiro valor: ').strip())
v2 = int(input('Digite o segundo valor: ').strip())
v3 = int(input('Digite o terceiro valor: ').strip())
v4 = int(input('Digite o quarto valor: ').strip())

values = (v1, v2, v3, v4)

'Adequando à proposta'

#1. Quantas vezes apareceu o valor 9

if values.count(9) > 0:

    print(f'''O valor 9 apareceu {values.count(9)} {'vez' if values.count(9) == 1 else 'vezes'}.''')

else:

    print(f'O valor 9 não foi digitado nenhuma vez.')

# 2. Em que posição foi digitado o primeiro valor 3

if values.count(3) != 0:

    print(f'O valor 3 foi digitado pela primeira vez na posição {values.index(3)}')

else:

    print(f'O valor 3 não foi digitado nenhuma vez.')

# 3. Quais foram os números pares.

par = ''
for v in values:

    if v % 2 == 0:

        par += f'{v} '

    else:

        par = 'NENHUM'


print(f'Os valores pares foram: {par} ')