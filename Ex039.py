# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar ao serviço militar
# Se já passou do prazo de alistamento

# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

# 1° Tratamento de dados sobre a idade informada

idade = input('Qual sua idade?')

if 'anos' in idade:

    idade = idade.split('anos')
    idade = ''.join(idade)

idade = int(idade)

# 2° Informação sobre o alistamento do serviço militar

if idade < 18:

    print(f'Faltam {18-idade} {("ano" if (18-idade) == 1 else "anos")}, para seu alistamento. ')

elif idade == 18:

    print(f'Está no período de você se alistar, compareça à junta militar mais próxima.')

else:

    print(f'Você excedeu o prazo de alistamento em {(idade-18)} {"ano" if (idade-18) == 1 else "ano"}.')
