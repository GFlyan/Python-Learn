#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

'Adequando à Propósta'

def ficha(name='<desconhecido>', gols=0):
    """
    -> A função ficha tem utilidade de retornar uma frase com o nome do jogador e quantos gols ele fez no campeonato

    :param name: Nome do jogador
    :param gols: Quantidade de gols feitos pelo jogador
    :return: Retorna o nome e a quantidade de gols feitas pelo jogador.
    """

    return f'O jogador {name} fez {gols} gols(s) no campeonato.'


'Mostrando Resultado'

print('-'*30)
player = input('Nome do Jogador: ').title()
amount_gols = input('Número de Gols: ')
print(ficha(player, amount_gols))
