#Crie um programa que leia dois valores e mostre um menu na tela:

#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos Números
#[5] Sair do Programa

#Seu programa deverá realizar a operação solicitada em cada caso.

from random import randint

#1° Valores fornecidos pelo usuário

v1, v2 = input(f'Digite dois valores (separados por espaço):').strip().split()
v1 = int(v1)
v2 = int(v2)
user = 0

#2° Escolha da operação pelo usuário

while user != 5:

    user = int(input(f'''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa   
    ''').strip())

    if user == 1:  #Somar

        print(f'{v1} + {v2} = {v1 + v2}')

    elif user == 2:  #Multiplicar

        print(f'{v1} x {v2} = {v1 * v2}')

    elif user == 3:  #Maior

        if v1 > v2:

            print(f'{v1} > {v2}')

        else:

            print(f'{v2} > {v1}')

    elif user == 4:  #Novos Números

        v1, v2 = input(f'Digite dois valores (separados por espaço):').strip().split()
        v1 = int(v1)
        v2 = int(v2)

    elif user == 5: #Finalizar programa

        print(f'Programa finalizado.')

    else: #Opção invalida

        print('Opção invalida.\nTente novamente.')