''' Listas

O que são as listas?

- São variáveis compostas que podem ser modificadas e são representadas
por []

Adição de elementos em lista na última posição

-Para adicionar um elemento em uma lista podemos usar o método append
<list>.append('x')

-Este método adiciona uma posição a mais na lista e o seu parâmetro será
o dado argumento 'x'

Adição de elementos em lista em uma dada posição

-Para adicionar um elemento à uma lista em uma posição específica
podemos utilizar o método <list>.insert(position, 'x')

-O argumento 'x' fornecido estará na posição 'position' fornecida
e o elemento que antes contido na posição agora ocupada pelo novo
argumento, estará na posição sucessora.

Deleção de elementos em uma lista

-Podemos utilizar o comando del <list>[position]

-Também o método pop <list>.pop(position)

-E também o método remove que diferentemente do comando del e do método pop,
recebe como paramêtro um argumento (<argument>)

Organização de elementos em uma lista

-O método <list>.sort() serve para organizar de forma ordenada
os elementos em uma lista [lembra a função sorted() sendo que
esta é derivada do método .sort()]

Backup de listas

-a-> lista

-b = a[:] // a variável composta b recebe todos os elementos da 'lista a',
sendo possível a manipulação da 'lista b' sem afetar a 'lista a' e vice
versa.

-Quando criamos <b = a> fazemos uma ligação entre as listas onde se afetar
uma afetará a outra.

Enumerate

-Enumerate é um função utilizada dentro de um laço para retornar a posição
de uma variável temporária e o valor atribuido a ela.

-for c, v enumerate(<list>)

c = contador da posição da lista
v = valor atribuido à variável para cada elemento da lista

'''

#Faça um programa que leia 5 valores numéricos e guarde-os
#em uma lista.

#No final, mostre qual foi o maior e o menor valor digitado e
#as suas respectivas posições na lista.

'Definições'

values = []

'Adequando à proposta'

for p in range(0, 5):

    values.append(input(f'Digite um valor para a Posição {p}: '))

print('-='*15)
print(f'Você digitou os valores: {values}')

'Mostrando resultados'

mayor_value = sorted(values)[-1]
minor_value = sorted(values)[0]

#Maior valor
print(f'O maior valor digitado foi {mayor_value} na posição', end=' ')

for c, v in enumerate(values):

    if v == mayor_value:

        print(f'{c}...', end=' ')

#Menor valor

print(f'\nO menor valor digitado foi {minor_value} na posição', end=' ')

for c, v in enumerate(values):

    if v == minor_value:

        print(f'{c}...', end=' ')