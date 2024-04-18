# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente

    # Console

    # Digite o nome: Ana Maria de Souza
    #primeiro: Ana
    #último: Souza

nome = input('Digite o nome: ').strip().split()
print(f'primeiro: {nome[0]}')
print(f'último: {nome[-1]}')