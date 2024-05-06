#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

'Adequando à Propósta'

def ficha(name='<desconhecido>', gols=0):

    return f'O jogador {name} fez {gols} gols(s) no campeonato.'

'Mostrando Resultado'

print('-'*30)
player = input('Nome do Jogador: ')
amount_gols = input('Número de Gols: ')
print(ficha(player, amount_gols))
