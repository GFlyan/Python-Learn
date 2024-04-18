# Desenvolva um programa que leia:
# Nome, idade e sexo de 4 pessoas.
# No final do programa mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

#Declarações

group = []
person = []
names = []
ages = 0
genders = []
old_men = []
young_women = 0
position = 0

#Lendo as informações das pessoas e armazenando as

for p in range(0, 4):

    name = input(f'Qual o nome da {p+1}ª pessoa? ').strip().capitalize()
    age = int(input(f'Qual a idade da {p+1}ª pessoa? ').strip())
    gender = input(f'A {p+1}ª  pessoa é HOMEM ou MULHER? ').strip().upper()
    ages += age
    person = [name, age, gender]
    group.insert(p, person)

#Condições

##Idade média do grupo

age_group = (ages // 4)

##Nome do homem mais velho e a quantidade de mulheres com menos de 20 anos


for p in group:

    if 'HOMEM' in p:

        old_men.insert(position, p[1])
        position += 1

    elif 'MULHER' in p:

        if p[1] < 20:

            young_women += 1

    old_men.sort()

#Visualização das condições

print(f'A idade média do grupo é {ages // 4} anos.')
print(f'A idade do homem mais velho do grupo é: {old_men[-1]} anos')
print(f'A quantidade de mulheres com menos de 20 anos no grupo é: {young_women} ')

