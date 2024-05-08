#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final mostre:

#1. Quantas pessoas tem mais de 18 anos
#2. Quantos homens foram cadastrados
#3. Quantas mulheres tem menos de 20 anos

#Definições

person = []
men = 0
old = 0
women_under_20 = 0

#Adequando à proposta

while True:

    print('-'*30)
    print(f'''{'CADASTRE UMA PESSOA':^30}''')
    print('-'*30)

    #Definindo idade

    age = int(input('Idade: ').strip())

    #Definindo sexo

    sex = ''

    while sex != 'M' and sex != 'F':

        sex = input('Sexo [M/F]: ').strip().upper()

    person = sex, age

    #Verificando maiores de idade

    if person[1] >= 18:

        old += 1

    #Verificando se é homem

    if person[0] == 'M':

        men += 1

    #Verificando mulheres abaixo de 20 anos

    if person[0] == 'F' and person[1] < 20:

        women_under_20 += 1

    #Verificando continuação do programa

    print('-' * 30)

    user = ''

    while user != 'N' and user != 'S':

        user = input('Quer continuar? [S/N] ').strip().upper()

    if user == 'N':

        break

#Mostrando resultados

print('-'*30)

#1. Quantas pessoas tem mais de 18 anos

print(f'''{'Nenhuma' if old == 0 else old} {'pessoas' if old > 1 else 'pessoa'} tem mais de 18 anos.''')

#2. Quantos homens foram cadastrados

print(f'''{'Nenhum' if men == 0 else men} {'homems' if men > 1 else 'homem' } {'foram cadastrados' if men > 1 else 'foi cadastrado'}.''')

#3. Quantas mulheres tem menos de 20 anos

print(f'''{'Nenhuma' if women_under_20 == 0 else women_under_20} {'mulheres' if women_under_20 > 1 else 'mulher'} tem menos de 20 anos.''')

print('-'*30)
