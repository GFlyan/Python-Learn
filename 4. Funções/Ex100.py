#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().

#A primeira função vai sortear 5 números e vai colocá-los dentro da lista.

#A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.



'Definições'

from random import choice
list_nums = list(range(0, 10))

'Adequando à proposta'

def sorteia(any_list):

    sorted_nums = list()
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        
        num_choice = choice(any_list)
        sorted_nums.append(num_choice)
        print(num_choice, end=' ')

    print('PRONTO!')
    return sorted_nums

def somaPar():

    print('-='*20)
    pairs = int()
    sorted_nums = sorteia(list_nums)
    for i in sorted_nums:

        if (i % 2) == 0:

            pairs += i

    print(f'Somando os valores pares de {sorted_nums}: {pairs}')
    print('-='*20)

'Mostrando resultados'

somaPar()