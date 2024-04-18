#Crie um programa onde o usuário possa digitar vários
#valorres numéricos e cadastre-os em uma lista.

#Caso o número já exista lá dentro, ele não será
#adicionado.

#No final, serão exibidos todos os valores numéricos
#digitados em ordem crescente.

'Definições'

values = []

'Adequando à proposta'

while True:

    while True:

        value = int(input('Digite um valor: '))

        if value in values:

            print('Valor duplicado! Insira outro número...')

        else:

            print('Valor adicionado com sucesso...')
            values.append(value)
            break

    user = None
    while user != 'N' and user != 'S':

        user = input('Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

'Mostrando resultados'

print('-='*20)
print(f'Você digitou os valores {sorted(values)}')