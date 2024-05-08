# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos:MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

# 1° Tratamento de dados sobre a idade fornecida

idade = input('Qual a sua idade?').strip()

if 'anos' in idade:

    idade = idade.split('anos')
    idade = ''.join(idade)

idade = int(idade)

# 2° Categoria em relação à classificação etária

if idade <= 9:

    print('MIRIM')

elif idade > 9 and idade <= 14:

    print('INFANTIL')

elif idade > 14 and idade <= 19:

    print('JUNIOR')

elif 19 > idade <= 25:

    print('SÊNIOR')

else:

    print('MASTER')