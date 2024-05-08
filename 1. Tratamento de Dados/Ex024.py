# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome da sua cidade: ').strip().split()

if cidade[0] == 'Santo':
    print('Sua cidade começa com "Santo".')
else:
    print('Sua cidade não começa com "Santo".')


