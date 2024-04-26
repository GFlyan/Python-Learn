#Crie um pograma que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feito em cada partida.
#No final, tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

'Definições'

player = dict()
gols = list()

'Adequando à proposta'

player['Nome'] = input('Nome do Jogador: ')
matchs = int(input('Total de partidas: '))

for p in range(matchs):

    gols.append(int(input(f'Quantos gols na {p+1}ª partida? ')))

player['Gols'] = gols
player['Total'] = sum(gols)

'Mostrando resultado'

print('-='*15)

for k, v in player.items():

    print(f'{k}: {v}')

print('-='*15)

print(f'O jogador {player['Nome']} jogou {matchs} partidas.')

for c, g in enumerate(gols):

    print(f'    => Na partida {c+1} fez {g, "gols" if g != 1 else g, "gol"}.')