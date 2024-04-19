#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastere-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescentee, além da idade, com quantos anos a pessoa vai se aposentar.

person = dict()

person['Nome'] = input('Nome: ')
person['Idade'] = 2024 - int(input('Ano de Nascimento: '))
person['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if person['CTPS'] != 0:

    person['Contratação'] = int(input('Ano de Contratação: '))
    person['Aposentadoria'] = 