# Laços de Repetição - Estrutura de Repetição com Variável de Controle

# laço c no intervalo(x, y): -> for c in range(x, y):
# c = variável de controle, é o contador da estrutura de repetição podendo ser representadod por qualquer índice
# tendo a unica função de indicar em qual ordem o código está dentro de um dado intervalo

# É possivel se referir a variável de controle, sendo que ela vai ser uma variável existente somente durante o momento da
# execução do laço.

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício.
# A contagem é de 10 até 0, com uma pausa de 1 segundo entre eles.

#Declarações

from time import sleep

#Contagem regressiva esperando 1 segundo entre cada contagem

for contagem in range(0, 11):

    print(10-contagem)
    sleep(1)

#Fim da contagem regressiva

print('!!!KABUM!!!')

