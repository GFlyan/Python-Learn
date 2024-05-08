 #Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

value = float(input('Digite o preço: R$'))
increase = int(input('Quantos porcento deseja aumentar: '))
depreciate = int(input('Quantos porcento deseja diminuir: '))
moeda.resumo(value=value, increase=increase, depreciate=depreciate)