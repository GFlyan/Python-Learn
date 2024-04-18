#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

'Definições'

from random import randint
from time import sleep
all_results = list()
results = list()

'Adequando à proposta'

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

user = int(input('Quantos jogos serão gerados? '))

for choice in range(user):

    for n in range(6):

        while True:

            result = randint(1, 60)
            if result not in results:
                results.append(result)
                break

    results.sort()
    all_results.append(results[:])
    results.clear()

'Mostrando resultados'
print('-='*15)

for c, r in enumerate(all_results):

    sleep(1)
    print(f'Jogo {c+1}: {r}')

print(f'{"BOA SORTE!":=^30}')