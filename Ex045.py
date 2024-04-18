# Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import choice

# Escolha do usuário entre: PEDRA, PAPEL e TESOURA

user = input('Pedra, papel ou tesoura?').upper().strip()

# Escolha da maquina entre: PEDRA, PAPEL e TESOURA

options = ['PEDRA', 'PAPEL', 'TESOURA']

machine = choice(options)

# Resultado da disputa

if user == 'PEDRA':

    if machine == 'PEDRA':

        print(f'EMPATE!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'PAPEL':

        print(f'VOCÊ PERDEU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'TESOURA':

        print(f'VOCÊ GANHOU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

elif user == 'PAPEL':

    if machine == 'PEDRA':

        print(f'VOCÊ GANHOU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'PAPEL':

        print(f'EMPATE!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'TESOURA':

        print(f'VOCÊ PERDEU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

elif user == 'TESOURA':

    if machine == 'PEDRA':

        print(f'VOCÊ PERDEU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'PAPEL':

        print(f'VOCÊ GANHOU!\nVocê escolheu: {user}\nO computador escolheu: {machine}')

    elif machine == 'TESOURA':

        print(f'EMPATE!\nVocê escolheu: {user}\nO computador escolheu: {machine}')
