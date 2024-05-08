#Melhore o jogo do Ex028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#Importando biblioteca e declarando variáveis

from random import randint
tryes = 1

#1°Valor escolhido pela máquina

machine = randint(0, 10)

#2° Valor escolhido pelo usuário

user = int(input(f'Escolha um valor para advinhar:').strip())

while user != machine:

    if machine > user:

        print(f'Digite um valor maior...')

    else:

        print(f'Digite um valor menor...')

    print(f'''Você errou {tryes} {'vez' if tryes == 1 else 'vezes'}!''')
    user = int(input(f'Escolha novamente um valor para advinhar:').strip())
    tryes += 1

#3° Resultado final

print(f'Você acertou!!!')

if tryes == 1:

    print(f'Foi necessário 1 única tentativa para você acertar!\n!!!INCRÍVEL!!!')

else:

    print(f'Foram necessárias {tryes} tentativas para você acertar!')
