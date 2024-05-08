#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:

#1. Qual é o total gasto na compra
#2. Quantos produtos custam mais de R$1000,00
#3. Qual é o nome do produto mais barato?

#Definições

summatory = 0
expansive = 0
cheap = ''
last_price = 0
total_products = 0

#Adequando à proposta

print('-'*30)
print(f'''{'LOJA SUPER BARATÃO':^30}''')

while True:

    total_products += 1
    print('-' * 30)
    product = input('Nome do Produto: ').strip()
    price = float(input('Preço: R$').strip())
    print('-'*30)

    #Total gasto

    summatory += price

    #Produtos mais caros que R$1000,00

    if price > 1000:

        expansive += 1

    #Nome do produto mais barato

    if total_products == 1 or price < last_price:

        cheap = product

    last_price = price

    #Continuação do programa

    user = ''

    while user != 'S' and user != 'N':

        user = input('Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

#Mostrando resultados

#1. Qual é o total gasto na compra

print(f'O total gasto na compra é de R${summatory:.2f}!')

#2. Quantos produtos custam mais de R$1000,00

print(f'''{'Nenhum' if expansive == 0 else expansive} {'produtos' if expansive > 1 else 'produto'} {'custam' if expansive > 1 else 'custa'} mais que R$ 1000,00!''')

#3. Qual é o nome do produto mais barato?

print(f'O produto mais barato é {cheap}!')

