#Faça um programa que tenha uma função chamada contador().
#A função receberá três parâmetros: inicio, fim  e passo e irá realizar a contagem

#Seu programa tem que realizar três  contagens através da função criada

#1. De 1 até 10, de 1 em 1
#2. De 10 até 0, de 2 em 2
#3. Uma contagem personalizada

'Adequando à proposta'

def contador(inicio, fim, passo):


    if inicio > fim:

            lista = list(range(fim, inicio, passo))
            lista = sorted(lista, reverse=True)
            print(lista)

    if fim > inicio:

        fim += 1
        lista = list(range(inicio, fim, passo))
        print(lista)


'Mostrando resultados'

#1. De 1 até 10, de 1 em 1

contador(inicio=1, fim=10, passo=1)

#2. De 10 até 0, de 2 em 2

contador(inicio=10, fim=0, passo=2)

#3. Uma contagem personalizada


