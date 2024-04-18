# Desenvolva um programa que leia seis números inteiros
# O programa deverá mostrar a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

#Definindo as listas e variáveis a serem utilizadas

numeros = []
soma_numeros_pares = 0 #Acumulador

#Digite 6 número inteiros

for ler in range(0, 6):

    ler += 1

    numero = input(f'Digite o {ler}° número: ')
    numeros += [numero]

#Mostrar somente os números inteiros

for num in numeros:

    #Somando somente os números pares
    num = int(num)

    if (num % 2) == 0:

        soma_numeros_pares += num

#Mostrando somente os números pares

print(f'A soma entre os números pares fornecidos é: {soma_numeros_pares}')


