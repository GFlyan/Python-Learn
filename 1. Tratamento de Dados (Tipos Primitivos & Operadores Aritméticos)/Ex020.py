#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

#1ª Resolução

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]

#A funçao shuffle(seq) necessita que a a lista ja esteja pré-definida para que seja embaralhada
#você pode especificá-la utilizando [] e salvando-a como uma variável que será definida como argumento de shuffle(lista)

shuffle(lista)

#Não se pode guardar shuffle em uma variável!

print(f'A ordem sorteada será {lista}!')

#Outra forma seria utilizando sample()
#sample(seq, n_loc)
#seq pode ser pré_definida em uma variavel lista[] ou definir as variaveis como argumentos de seq (a,b,c)
    #neste caso a sintaxe seria sample((a, b, c, d), 4)
        #4 por que são 4 argumentos