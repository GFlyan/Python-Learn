#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastere-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescentee, além da idade, com quantos anos a pessoa vai se aposentar.

#dict -> -nome -idade -ctps -contratação -salário aposentadoria

'Definições'

from datetime  import datetime
person = dict()

'Adequando à proposta'

person['Nome'] = input('Nome: ')
date_born = int(input('Ano de Nascimento: '))
current_year = datetime.now().year
person['Idade'] = current_year - date_born
person['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if person['CTPS'] > 0:

    person['Contratação'] = int(input('Ano de Contratação: '))
    person['Salário'] = float(input('Salário: R$'))
    person['Aposentadoria'] = person['Contratação']+ 35 - date_born

'Mostrando resultado'

print('-='*15)

for k, v in person.items():

    print(f'{k}: {v}')
    

