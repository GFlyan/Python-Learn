# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# 1° Tratamendo de dados sobre o valor do empréstimo

empréstimo = input('Qual será o valor do empréstimo? R$').strip()

if ',' in empréstimo:

    empréstimo = empréstimo.replace(',', '.')

empréstimo = float(empréstimo)


# 2° Tratamento de dados sobre o salário do cliente

salário = input('Quanto é seu salário mensal? R$').strip()

if ',' in salário:

    salário = salário.replace(',', '.')

salário = float(salário)

# 3° Tratamento de dados sobre o tempo de pagamento do empréstimo

tempo = int(input('Em quantos anos pretende quitar o empréstimo?'))

# Condição de empréstimo

meses = tempo*12
prestação_mensal = empréstimo/meses

if prestação_mensal <= (salário * 30 / 100):

    print(f'O empréstimo de R${empréstimo:.2f} será concedido à você desde que seja quitado em {tempo} anos.')
    print(f'O valor da prestação mensal é R${prestação_mensal:.2f}.')

else:

    print(f'O empréstimo de R${empréstimo:.2f} não pode ser concedido à você, pois a parcela mensal é maior que 30% do seu salário mensal.')
    print(f'O valor da prestação mensal é R${prestação_mensal:.2f}.')

