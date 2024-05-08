# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

    #Console:

    #Digite um número: 1834
    #unidade:4
    #dezena:3
    #centena:8
    #milhar: 1

# Método 1: Utilizar métodos de tratamento de cadeias de caractéres

número1 = input('Digite um número entre 0 e 9999: ').strip()

if len(número1) == 4:
    print(f'unidade: {número1[3]}')
    print(f'dezena: {número1[2]}')
    print(f'centena: {número1[1]}')
    print(f'milhar: {número1[0]}')

elif len(número1) == 3:
    print(f'unidade: {número1[3]}')
    print(f'dezena: {número1[2]}')
    print(f'centena: {número1[1]}')

elif len(número1) == 2:
    print(f'unidade: {número1[3]}')
    print(f'dezena: {número1[2]}')


elif len(número1) == 1:
    print(f'unidade: {número1[3]}')

# Existe a forma matemática