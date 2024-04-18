# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = str(input('Digite o ano desejado para saber se ele é bissexto:')).strip()
ano = int(ano)

#Análise bissextuária

if (ano%100) == 0:

    if (ano%400) == 0:

        print(f'O ano {ano} é bissexto!')

    else:

        print(f'O ano {ano} não é bissexto.')

else:

    if (ano%4) == 0:

        print(f'O ano {ano} é bissexto!')

    else:

        print(f'O ano {ano} não é bissexto.')