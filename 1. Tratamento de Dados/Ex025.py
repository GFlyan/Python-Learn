# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

# Forma 1

nome = input('Digite seu nome completo: ').strip()
verificador = 'Silva' in nome

if verificador == True:
    print('Seu nome tem "Silva"!')
else:
    print('Seu nome não tem "Silva".')

# Forma 2

nome2 = input('Digite o nome completo do seu pai: ')

if nome2.find('Silva') == -1:
    print('O nome do seu pai não tem "Silva".')
else:
    print('O nome do seu pai tem "Silva"!')

