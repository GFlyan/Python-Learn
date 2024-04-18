# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

#Escolha da base de conversão

num_int = int(input('Digite um número inteiro para ser convertido:'))
base_escolhida = int(input('Escolha uma número referente à base de conversão desejada:\n1 -> Binária\n2 -> Octal\n3 -> Hexadecimal\nQual sua escolha?\n'))

# Conversão Binária

if base_escolhida == 1:

    print(f'{num_int} convertido para binário:\n{bin(num_int)[2:]}')

# Conversão Octal

elif base_escolhida == 2:

    print(f'{num_int} convertido para octal:\n{oct(num_int)[2:]}')

# Conversão Hexadecimal

elif base_escolhida == 3:

    print(f'{num_int} convertido para hexadecimal:\n{hex(num_int)[2:]}')