#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().

#A primeira função vai sortear 5 números e vai colocá-los dentro da lista.

#A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

'Definições'

from random import randint
list_nums = list()

'Adequando à proposta'

def sorteia():

    c = int()
    while True:

        num_sorted = randint(0,10)

        if num_sorted not in list_nums:

            list_nums.append(num_sorted)
            c += 1

        if c == 5:

            break

    print(f'Os números sorteados foram {list_nums}')
    return list_nums


def somaPar():

    print('-='*20)
    pairs = int()
    sorteia()
    for i in list_nums:

        if (i % 2) == 0:

            pairs += i

    print(f'A soma entre os números pares da lista é: {pairs}')
    print('-='*20)

'Mostrando resultados'

somaPar()