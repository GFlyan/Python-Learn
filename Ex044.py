# Elabore um programa que calcule o valor à ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

# Valor normal do produto

normal_value = input('Digite o valor do produto:').strip()

## Tratamento de dados do valor normal fornecido do produto

if 'R$' in normal_value:

    normal_value = normal_value.replace('R$', '')

if ',' in normal_value:

    normal_value = normal_value.replace(',', '.')

normal_value = float(normal_value)

# Seleção de forma de pagamento

print('Você possui as seguintes formas de pagamento:\n1 - À vista dinheiro/cheque: 10% de desconto\n2 - À vista no cartão: 5% de desconto\n3 - Em até 2x no cartão: Preço normal\n4 - 3x ou mais no cartão: 20% de juros')
payment = int(input('Selecione uma forma de pagamento:').strip())

# 1° Forma de pagamento - À vista no dinheo/cheque: 10% de desconto

if payment == 1:

    final_value = normal_value - (10*normal_value/100)
    print(f'O valor a ser pago será de R${final_value}!')

# 2° Forma de pagamento - À vista no cartão: 5% de desconto

elif payment  == 2:

    final_value = normal_value - (5*normal_value/100)
    print(f'O valor a ser pago será de R${final_value}!')

# 3° Forma de pagamento - Em até 2x no cartão: valor normal

elif payment == 3:

    final_value = normal_value
    print(f'O valor a ser pago será de R${final_value}!')

# 4° Forma de pagamento  -  3x ou mais no cartão: 20% de juros

elif payment == 4:

    final_value = normal_value + (20*normal_value/100)
    print(f'O valor a ser pago será de R${final_value}!')

else:

    print('Você escolheu uma opção inexistente.')



