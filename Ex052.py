# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Digite um número para saber se ele é ou não um número primo:\n'))

#Acumulador utilizado

verication_primo = 0

#Algoritmo de existenia de um número primo

for x in range(0, numero):

    x += 1

    if (numero % x) == 0:

        verication_primo += 1

#Verificação de número primo

if verication_primo <= 2:

    print(f'O número {numero} é um número primo!')

else:

    print(f'O número {numero} não é um número primo.')

