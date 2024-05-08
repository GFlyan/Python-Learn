# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso tidos.

#Definindo variáveis a serem utilizadas

weights = []

#Lendo o peso de 5 pessoas

for person in range(0, 5):

    weight = float(input(f'{person+1}ª pessoa, digite seu peso: KG '))
    weights += [weight]

#Atribuindo o menor e maior peso

minor_weight = (sorted(weight))[-1]
major_weight = (sorted(weight))[0]

#Mostrando o maior e menor peso

print(f'O maior peso obtido foi: KG {major_weight:.2f}\nO menor peso obtido foi: KG {minor_weight:.2f}')
