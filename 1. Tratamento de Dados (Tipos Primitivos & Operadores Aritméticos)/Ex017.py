#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#1ª Resolução

from math import pow, sqrt

co = float(input('Qual o valor do cateto oposto do triângulo? '))
ca = float(input('Qual o valor do cateto adjacente do triângulo? '))

hip = sqrt(pow(co, 2)+pow(ca, 2))

print(f'O valor da hipotenusa é {hip:.2f}!')

#2ª Resolução

co2 = float(input('Qual o valor do cateto oposto do triângulo? '))
ca2 = float(input('Qual o valor do cateto adjacente do triângulo? '))

hip2 = ((co**2)+(ca**2))**1/2

print(f'O valor da hipotenusa é {hip:.2f}!')

#3ª Resolução

#math possui uma função específica para o cálculo da hipotenusa
#hypot(a, b) requer dois argumentos, tal que a: cateto oposto, b: cateto adjacente

from math import hypot

co = float(input('Qual o valor do cateto oposto do triângulo? '))
ca = float(input('Qual o valor do cateto adjacente do triângulo? '))

hip = hypot(co, ca)

print(f'O valor da hipotenusa é {hip:.2f}!')