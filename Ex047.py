# Crie um programa que mostre na tela:
# Todos os números pares que estão no intervalo entre 1 e 50


#Lista para armazenar os números pares

numeros_pares = []

#Contagem de números pares contidos em um dado intervalo

for numero in range(0, 50):

    numero += 1
    if (numero % 2) == 0:

        numeros_pares += [numero]

#Mostrar a lista de números

# numeros_pares = numeros_pares.split()
print(numeros_pares)