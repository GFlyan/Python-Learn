#Tipos primitivos são funções que podem modificar o valor de algo.
#Os tipos primitivos em Python podem ser:
#str() -> Modificar o valor para texto (necessário a utilização de aspas quando for atribuir para indentificar como string)
#int() -> Modificar o valor para número inteiro (0, 1, 2, 3, ...)
#float() -> Modificar o valor para número de ponto flutuante (0,1; 1,2; 3,4; ...)
#bool() -> Modificar o valor para um valor lógico (True or False | verdadeiro ou falso)

#Faça um programa que peça dois valores e em seguida mostre a soma entre eles, e depois a diferença entre os mesmos

num1 = int(input('Digite um valor:'))
num2 = int(input('Digite outro valor:'))
#input() é uma função de valor = str()
#necessário utilizar a função int() para que seja possível a realização de operações aritméticas
soma = num1+num2
#A variável 'soma' irá realizar a operação de soma entre a variável 'num1' e 'num2'.
print(f'A soma entre {num1} e {num2} vale {soma}.')
dif = num1-num2
#A variável 'dif' irá realizar a operação de subtração entre a variável 'num1' e 'num2'.
print(f'A diferença entre {num1} e {num2} é {dif}.')

#Se não modificar o valor de input() nas linhas que se pede o valor desejado, as variáveis receberão um valor str()
#str(x) quando somada (+) a outra str(y) realiza uma contatenação (junção) das duas strings.