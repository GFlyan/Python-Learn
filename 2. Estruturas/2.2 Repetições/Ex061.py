#Refaça o Ex051, lendo o primeiro termo e a razão de uma PA.
#Mostre os 10 primeiros termosda progressão usando a estrutura 'while'.
#Equação de uma PA: an = a1+(n-1)*r

#Declarando variáveis

an = 0
n = 1
terms = []

#Informações fornecidas pelo usuário segundo o enunciado

a1 = int(input(f'Digite o primeiro termo da PA: ').strip())

r = int(input(f'Digite a razão da PA: ').strip())

#Adequando a estrutura a lei de formação da PA

while an != (a1+(10-1)*r):

    an = a1+(n-1)*r
    terms += [an]
    n += 1

#Resultado da PA

print(f'Os 10 primeiros termos da PA, dos dados fornecidos formam a seguinte sequência: {terms}')

