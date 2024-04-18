# Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário acertou ou errou.

from random import randint

# 1° Escolha do número pelo computador

número_computador = randint(0, 5)

# 2° Escolha do número pelo usuário

número_usuário = int(input('Digite um número:'))

# 3° Resultado

if número_usuário == número_computador:

    print(f'Parabéns!\nVocê escolheu o número correto.')

else:

    print(f'Que pena...\nVocê escolheu o número errado! \nO número escolhido foi {número_usuário} e o número correto era {número_computador}.')