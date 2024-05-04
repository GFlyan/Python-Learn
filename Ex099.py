#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros

#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'Adequando à proposta'

def maior(ints):

    print(f'Forma informados {len(ints)} valores ao todo.')
    mayor = int()
    for c, n in enumerate(ints):

        if c == 0:

            mayor = n

        else:

            if n > mayor:

                mayor = n

    print('-'*30)
    print(f'O maior valor informado foi {mayor}')
    print('-'*30)


nums = list()

while True:

    print('-='*15)
    nums.append(int(input('Digite um número: ')))

    user = None
    while user != 'N' and user != 'S':

        user = input('Você quer continuar? [S/N] ').upper()
        if user != 'N' and user != 'S':

            print('Não entendi...', end=' ')

    if user == 'N':

        break

'Mostrando resultados'

maior(nums)