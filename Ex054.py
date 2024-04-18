# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores
# Maioridade considerada a partir de 21 anos

#Declarando módulos e variáveis utilizadas

from datetime import date as dt
actual_year = dt.today().year
minority_people = 0
majority_people = 0

#Lendo o ano de nascimento de sete pessoas

for person in range(0, 7):

    year_born = int(input(f'{person+1}ª pessoa, digite o ano do seu nascimento: '))
    majority_check = actual_year - year_born

#Definindo quem é menoritario ou maioritario

    if majority_check >= 21:

        print(f'Você atingiu a maioridade!')
        majority_people += 1

    else:

        print(f'Você ainda está na menoridade.')
        minority_people += 1

    print('-'*40)

#Mostrando a quantidade de menores e maiores

print(f'{majority_people} pessoas atingiram a maioridade.\n{minority_people} pessoas ainda estão na menoridade.')
