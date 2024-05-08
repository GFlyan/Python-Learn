#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla

#Depois disso, mostre a listagem de números geradores e também indique o menor e o maior valor que estão na tupla

#Definições

from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

#Adequando à proposta

numbers = (n1, n2, n3, n4, n5)

#Mostrar listagem

print(f'Os números sorteados foram: {numbers}')

#Mostrar menor e maior valor da tupla

print(f'O menor valor é: {sorted(numbers)[0]}\nO maior valor é: {sorted(numbers)[-1]}')
