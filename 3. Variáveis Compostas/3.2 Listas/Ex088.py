#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
#serão gerados e vai sortear entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

'Definições'

from time import sleep
from random import randint

result = list()
all_results = list()

'Adequando à proposta'

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

user = int(input('Quantos jogos serão gerados? '))

for choice in range(user):
    
    for numbers in range(6):

        while True:

            number = (randint(1, 60))

            if number not in result:

                result.append(number)
                break

    result.sort()
    all_results.append(result[:])
    result.clear()

'Mostrando Resultados'

print('-='*15)

for c, r in enumerate(all_results):

    print(f'Jogo {c+1}: {r}')
    sleep(1.0)

print(f'{"< BOA SORTE! >":=^30}')