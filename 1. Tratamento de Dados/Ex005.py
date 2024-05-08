#Opereadores aritméticos:

#Existem vários tipos de operadores, dentre elees os ARITMÉTICOS que servem para fazer operações atiméticas

# + -> Realiza a SOMA de números e concatenação de strings
# - -> Realiza a SUBTRAÇÃO de números
# * -> Realiza a MULTIPLICAÇÃO entre dois termos, pode ser usado para repetir strings
# / -> Realiza a DIVISÃO entre dois números
# ** -> Realiza a POTENCIAÇÃO de um número elevado à outro
# // -> Realiza a DIVISÃO INTEIRA sem direito a resto
# % -> Mostra somente o resto que não é mostrado na DIVISÃO INTEIRA

#A ordem de efetuação das operações segue:

# ()
# **
# * / // %
# + -

##Arredondamento utilizando .format():
#
# {:.xf} | x = número de casas decimais que se quer formatar
#round(x, y) só funciona para arredondar números que ja possuem casas decimais

##Não quebrar a linha de print:
#end=' '
#Pode se ter um argumento dentro de (' ').

##Quebrar a linha do print:
#\n

##Fazer um valor aparecer dentro de X caractéres utilizando .format():
#{:x} | x = quantidade de caracteres que quer que apareça
#Ainda pode se usar metodos de alinhamento:
#{:<x} para alinhar para a esquerda dentro de X caractéres
#{:>x} para alinhar para a direita dentro de X caractéres
#{:^x} para alinhar para o centro dentro de X caractéres
#{:=^x} ficará alinhado ao centro e os espaços que não tiverem caractéres serão substituidos por '='


#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

num = int(input('Digite um número: '))

suc = num+1
ant = num-1

print(f'O sucessor de {num} é {suc} e seu antecessor é {ant}.')