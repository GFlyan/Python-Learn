# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso ideal
# Entre 25 até 29.9: Sobrepeso
# Entre 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

# 1° Tratamento de dados sobre o peso fornecido

peso = input('Qual o seu peso?').strip()

if ',' in peso:

    peso = peso.replace(',', '.')

if 'kg' in peso:

    peso = peso.split('kg')
    peso = ''.join(peso)

peso = float(peso)

# 2° Tratamento de dados sobre a altura fornecidad

altura = input('Qual a sua altura?').strip()

if ',' in altura:

    altura = altura.replace(',', '.')

altura = float(altura)

# 3° Análise do IMC

IMC = (peso / (altura ** 2))

if IMC < 18.5:

    print('Você está abaixo do peso.')

elif 25> IMC >= 18.5:

    print('Você está com o peso ideal.')

elif 30 > IMC >= 25:

    print('Você está com sobrepeso.')

elif 40 > IMC >= 30:

    print('Você está com obesidade.')

else:

    print('Você está com obesidade mórbida.')

print(f'Seu IMC é {IMC:.1f}!')