#Modifique as funções que foram criadas no Ex107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no Ex108

import moeda

value = float(input('Digite o preço: R$'))
increase = int(input('Quantos porcento deseja aumentar: '))
depreciate = int(input('Quantos porcento deseja diminuir: '))
print('-='*15)
print(f'A metade de {value} é {moeda.metade(value=value, format=True)}')
print(f'O dobro de {value} é {moeda.dobro(value=value, format=False)}')
print(f'Aumentando {increase}%, temos {moeda.aumentar(value=value, increase=increase, format=True)}')
print(f'Reduzindo {depreciate}%, temos {moeda.diminuir(value=value, depreciate=depreciate, format=False)}')
print('-='*15)



