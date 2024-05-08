# Faça um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas as letras minúsculas
    # Quantas letras ao todo, sem considerar os espaços
    # Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculo:', nome.upper())
print('Seu nome em minúsculo:', nome.lower())
nome = nome.split()

# Estrutura de repetição
quantidade_letras = 0  # Variável armazenadora
for i in nome:
    quantidade_letras += len(i)

print(f'Seu nome tem {quantidade_letras} letras.')
print(f'Seu primeiro nome é {nome[0]} e tem {len(nome[0])} letras.')

# Existe outra forma