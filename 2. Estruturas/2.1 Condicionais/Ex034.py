# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00. Calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

# 1° Tratameto de dados sobre o salário fornecido

salário = input('Quanto é seu salário? R$')

if (',' in salário) == True:

    salário = salário.replace(',', '.')

salário = float(salário)

# 2° Cálculo do aumento salarial

if salário > 1250:

    print(f'Você receberá um aumento de 10% que corresponde a R${(salário * 10 / 100) :.2f}, totalizando seu salário em R${(salário + (salário * 10 / 100)):.2f}!')

else:

    print(f'Você receberá um aumento de 15% que corresponde a R${(salário * 15 / 100):.2f}, totalizando seu salário em R${(salário + (salário * 15 / 100)):.2f}!')




