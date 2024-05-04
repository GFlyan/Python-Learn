#Faça um programa que tenha uma função chamada contador().
#A função receberá três parâmetros: inicio, fim  e passo e irá realizar a contagem

#Seu programa tem que realizar três  contagens através da função criada

#1. De 1 até 10, de 1 em 1
#2. De 10 até 0, de 2 em 2
#3. Uma contagem personalizada

'Definições'

from time import sleep

'Adequando à proposta'

def contador(inicio, fim, passo):

        if passo < 0:

                passo *= (-1)

        if passo == 0:

                passo = 1

        print('-='*15)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

        if inicio < fim:

                while inicio <= fim:
                        
                        print(inicio, end= ' ')
                        inicio += passo
                        sleep(1)

                print('FIM!')

        elif inicio > fim:

                while inicio >= fim:

                        print(inicio, end= ' ')
                        inicio -= passo
                        sleep(1)

                print('FIM!')

'Mostrando resultados'


#1. De 1 até 10, de 1 em 1

contador(inicio=1, fim=10, passo=1)

#2. De 10 até 0, de 2 em 2

contador(inicio=10, fim=0, passo=2)

#3. Uma contagem personalizada


print('-='*15)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))

contador(inicio=inicio, fim=fim, passo=passo)
