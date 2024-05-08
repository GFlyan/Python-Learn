# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior.
# O segundo valor é maior.
# Não existe valor maior, os dois são iguais.

# 1° Tratamento de dados sobre os valores fornecidos

num1, num2 = input('Digite dois números inteiros:').split()
num1 = int(num1)
num2 = int(num2)

# 2° Condição de comparação

if num1 > num2:

    print(f'O primeiro valor é maior.')

elif num1 == num2:

    print(f'Não existe valor maior, os dois são iguais.')

else:

    print(f'O segundo valor é maior.')
