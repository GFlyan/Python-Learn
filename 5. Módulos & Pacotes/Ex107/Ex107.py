'''
Modularização

-> Tem foco principal em dividir um sistema grande no intuito de aumentar a organização e a legibilidade do código facilitando a manutenção.
 
-> Todo arquivo .py dentro do projeto pode ser potencialmente um módulo.

Pacotes

-> Tem foco de organizar os módulos em diferentes vertentes.

-> Toda pasta no mesmo arquivo do projeto principal pode ser potencialmente um pacote.

'''

#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

#Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

value = float(input('Digite o preço: R$'))
increase = int(input('Quantos porcento deseja aumentar: '))
depreciate = int(input('Quantos porcento deseja diminuir: '))
print('-='*15)
print(f'A metade de {value} é {moeda.metade(value=value)}')
print(f'O dobro de {value} é {moeda.dobro(value=value)}')
print(f'Aumentando {increase}%, temos {moeda.aumentar(value=value, increase=increase)}')
print(f'Reduzindo {depreciate}%, temos {moeda.diminuir(value=value, depreciate=depreciate)}')
print('-='*15)



