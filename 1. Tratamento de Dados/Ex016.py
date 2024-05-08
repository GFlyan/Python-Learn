#A importação de bibliotecas serve para que você utilize diversas variáveis e funções já pré-definidas

#Você pode importar uma biblioteca de duas formas:
#1° import 'biblioteca' -> Vai importar todas as funcionalidades da biblioteca
#2° from 'biblioteca' import 'algo' -> Vai importar algo específico da biblioteca
   #Quando esta forma de importação for utilizada, não será necessário utilizar o objeto de módulo para utilizar a função desejada
#3° import 'biblioteca' as 'bt' -> Nova nomeação do módulo, como você vai querer chamar o objeto de módulo

#Uma das bibliotecas mais famosas do Python é a biblioteca math.

#Ela dispõe de diveras funcionalidades matemáticas tais como:

#ceil() -> Arredonda um número para cima
#floor() -> Arredonda um número para baixo
#trunc() -> Exclui as casas decimais de um número sem arredondá-lo
#pow(x, y) -> Realiza a função de exponenciação de dois números, sendo o primeiro argumento a base e o segundo o expoente
#sqrt(x) -> Realiza a função de raíz quadrada
#factorial() -> Realiza a função de fatorial de um número
#e muitas outras funções...

#Uma BIBLIOTECA é também conhecida como um MÓDULO
#Após a importação do módulo é criado um OBJETO DE MÓDULO que será a própria biblioteca
#Para se utilizar uma função de um módulo é necessário utilizar a sintaxe:
#nome_do_módulo.função_do_módulo()
#Exemplo: math.pow(2, 3)
#Para usar algo contido em um módulo se utiliza .

#Biblioteca random -> escolhe um número aleatório

#Você pode utilizar as bibliotecas nativas do Python ou baixar bibliotecas criadas por usuários no PyPI




#Faça um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

#Ex:
#Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.

#1ª Resolução

from math import trunc

num1 = float(input('Digite um número: '))

print(f'O número {num1} tem a parte inteira {trunc(num1)}.')

#2ª Resolução

num2 = float(input('Digite um número: '))

print(f'O número {num2} tem a parte inteira {num2:.0f}.')

#3ª Resolução

num3 = float(input('Digite um número: '))

print(f'O número {num3} tem a parte inteira {int(num3)}.')