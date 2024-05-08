#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Exemplo: 5! = 5x4x3x2x1 = 120

#Declaração de variáveis utilizadas

factorial = 1

#Número escolhido pelo usuário

user = int(input('Digite um valor para saber seu fatorial: ').strip())
backup_user = user

#Aplicação do fatorial

while user != 0:

    factorial *= user
    user -= 1

#Mostrando o resultado

print(f'{backup_user}! =  {factorial}')

