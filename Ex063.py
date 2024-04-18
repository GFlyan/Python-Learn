#Escreva um programa que leia um número n inteiro qualquer
#Mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

#Declarando variáveis

a0 = 0
a1 = 1
an = 0
sequence = [a0, a1]

#Informações fornecidas pelo usuário

order = int(input(f'Digite até que posição numérica você deseja visualizar a Sequência de Fibonacci: ').strip())

#Adequando a sequência

while (len(sequence)) != order:

    an = a0 + a1
    sequence += [an]
    a0 = a1
    a1 = an

#Mostrando o resultado

print(sequence)