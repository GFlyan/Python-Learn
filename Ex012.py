#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

product = float(input('Qual o valor do produto? R$ '))

desconto_product = product*5/100

new_value = product-desconto_product

print(f'O valor do produto após a aplicação do desconto de 5% é R${new_value:.2f}.')