# Faça um programa que calcule e a soma enre:
# Todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500.

#Lista de números ímpares multiplos de três contidas em um dado intervalo

list_num = []

#Contagem de números ímpares

for numero in range(1, 500):

    if (numero % 2) != 0 and (numero % 3) == 0:

        list_num += [numero]
        print(list_num)

#Somar todos os elementos da lista de números

print(f'A soma entre todos os números ímpares que são multiplos de 3 encontrados no intervalo (1, 500) é: {sum(list_num)}')

