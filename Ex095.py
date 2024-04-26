#Aprimore o Ex093 para que ele funcione com vários jogadores, incluindo um sistema de detalhes do aproveitamento de cada jogador.

'Definições'

players = list()
player = dict()
gols = list()

'Adequando à proposta'

while True:
    
    print('='*30)
    player['Nome'] = input('->Nome do jogador: ').capitalize()
    matchs = int(input(f'->Quantas partidas {player["Nome"]} jogou? '))
    
    print('-='*15)
    for m in range(matchs):

        gols.append(int(input(f'Quantos gols {player["Nome"]} fez na {m+1}ª partida? ')))
    print('-='*15)

    player['Gols'] = gols.copy()
    player['Total'] = sum(gols)

    players.append(player.copy())
    gols.clear()

    user = None
    while user != 'S' and user != 'N':

        user = input('->Quer continuar? [S/N] ').upper()

    if user == 'N':

        break

'Mostrando resultados'

print('='*40)
print(f'COD {"NOME":<15}{"GOLS":<15}TOTAL')
print('='*40)
for c, p in enumerate(players):

    print(f'{c+1}   {p["Nome"]:<15}{p["Gols"]}  {p["Total"]:>5}')
print('-'*40)

user = None
while True:

    user = input('-> Você quer ver os dados detalhados de algum jogador? [S/N] ').upper()

    if user == 'S':

        user = None

        while True:

            user = int(input('-> Você deseja ver os dados de qual jogador? COD  ')) - 1

            if user > len(players):

                print('Jogador não encontrado...')

            else: 

                break
        
        print('-'*40)
        print(f'Dados de {players[user]["Nome"]}')

        for c, g in enumerate(players[user]["Gols"]):

            print(f'    {c+1}º jogo: {g} {"gols" if g != 1 else "gol"}')
        
        print('-'*40)
        
    elif user == 'N':

        print('*'*40)
        break

