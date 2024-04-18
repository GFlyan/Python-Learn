'''Variáveis Compostas

Variáveis compostas, diferentemente das variáveis simples, são variáveis que podem
receber mais de uma atribuição ao seu valor, podendo ter n elementos atribuídos.

São constituídas por posições, como as posições em uma string (cadeia de caractéres)
Sendo que a primeira posição corresponde a posição 0, a segunda a posição posição 1
e assim adiante.

Existem 3 tipos de variáveis compostas:

°Tuplas

-> São representadas por ()
-> São imutáveis

°Listas

-> São representadas por []
-> São mutáveis


°Dicionários

-> São representados por {}


'''


''' Tuplas

O que são tuplas?
->Variáveis compostas imutáveis representadas por () 

Organização dos elementos de uma tupla
->sorted(<tuple>) // Organiza em ordem

Concatenação de tuplas:
<tuple1> += <tuple2> // <tuple3> = <tuple1> + <tuple2> 

Iteração com tuplas
for x in <tuple> // for x in range (0, len(<tuple>)

Contagem de elementos nas tuplas
<tuple>.count(x) // Retorna a quantidade do parâmetro passado
contido na tupla referenciada

Análise de elementos em tuplas
<tuple>.index(x) // Retorna a posição do elemento fornecido
como parâmetro

Deletação de tuplas
del(<tuple>)

'''

#Crie um programa que tenha uma tupla totalmente preenchida
#com uma contagem por extensão de zero até vinte.

#Seu programa deverá ler um número pelo teclado [entre 0 e 20]
#e mostrá-lo por extenso

#Definições

numbers = (
'zero',
'um',
'dois',
'três',
'quatro',
'cinco',
'seis',
'sete',
'oito',
'nove',
'dez',
'onze',
'doze',
'treze',
'quatorze',
'quinze',
'dezesseis',
'dezessete',
'dezoito',
'dezenove',
'vinte')

#Adequando a proposta

while True:

    while True:

        user = int(input('Digite um número entre 0 e 20: ').strip())

        if 0 <= user <= 20:

            break

        print('Tente novamente...', end=' ')


    print(f'O número {user} por extenso é: {numbers[user].upper()}!')

    exit = input('Você deseja continuar? ').strip().upper()

    if exit == 'NAO':

        break