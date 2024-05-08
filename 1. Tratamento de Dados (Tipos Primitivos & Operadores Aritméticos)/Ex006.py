#Faça um programa que leia um número e mostre sua metade, seu dobro, triplo e raiz quadrada

num = int(input('Digite um valor numérico para descobrir sua metade, seu dobro, triplo e sua raiz quadrada: '))

mid = (num/2)
double = (num*2)
triple = (num*3)
sqrd = (num**(1/2))

print(f'A metade de {num} é {mid}, seu dobro é {double}, triplo {triple} e sua raiz quadrada {sqrd:.2f}!')

#pow(a, b) realiza a função de exponenciação sendo necessário dois parametros, onde o primeiro é a base e o segundo o expoente

