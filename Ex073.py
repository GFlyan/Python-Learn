#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol
#na ordem de colocação.

#Depois mostre:
#1. Apenas os 5 primeiros colocados
#2.Os últimos 4 colocados da t0abela
#3.Uma lista com os time em ordem alfabética
#4. Em que posição da tabela está o time da Chapecoense

#Definições

brasileirao = (
'Palmeiras',
'Grêmio',
'Atlético Mineiro',
'Flamengo',
'Botafogo',
'Red Bull Bragantino',
'Fluminense',
'Athletico Paranaense',
'Internacional',
'Fortaleza',
'São Paulo',
'Cuiabá',
'Corinthians',
'Cruzeiro',
'Vasco da Gama'
'Bahia',
'Santos',
'Goiás',
'Coritiba',
'América Mineiro')

#Adequando à proposta

print('-='*30)
print(f'Lista de time do Brasileirão: {brasileirao}')
print('-='*30)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-='*30)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*30)
print(f'''O Flamengo está na {brasileirao.index('Flamengo')+1}ª posição.''')
