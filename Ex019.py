#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

#1ª Resolução

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

#A função choice() sorteia valores especificados como argumentos dentro de ()
#choice(seq) = choiche((x, y, z))
#Essa sintaxe é necessária pois choice necessita de uma sequência que é tida como um único parametro
#(x, y, z) seria o parametro seq = sequencia

sorteado = choice((a1, a2, a3, a4))
print(f'O aluno escolhido para apagar o quadro foi: {sorteado}!')

#2ª Resolução

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1, n2, n3, n4]
#Listas em python ficam entre colchetes

srtd = choice(lista)

print(f'O aluno escolhido para apagar o quadro foi: {srtd}!')

