#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#Definições

from random import randint
win = 0

#Adequando à proposta

print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')

while True:

    print('-=' * 15)
    user_value = int(input('Digite um valor: ').strip())
    user_choice = ''

    while user_choice != 'I' and user_choice != 'P':

        user_choice = input('Par ou ímpar? [P/I] ').strip().upper()

    print('-'*30)
    machine_value = randint(0, 10)
    machine_choice = ('I' if user_choice == 'P' else 'P')
    lets_sum = user_value + machine_value
    result = 'PAR' if (lets_sum % 2) == 0 else 'IMPAR'
    print(f'Você jogou {user_value} e o computador {machine_value}. Total de {lets_sum} DEU {result}.')
    print('-'*30)

    if result[0] == user_choice:

        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        win += 1

    else:

        print('Você PERDEU!')
        print('-=' * 15)
        break

#Mostrando resultado

print(f'''GAME OVER! Você venceu {'nenhuma' if win == 0 else win} {'vezes' if win != 1 and win != 0 else 'vez'}.''')
