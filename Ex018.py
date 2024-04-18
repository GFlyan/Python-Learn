#Faça um programa que leia um ângulo qualquer e mostre na tela seu seno, cosseno e tangente

from math import radians, sin, cos, tan
#As funções tan(), sin() e cos() calculam respectivamente o valor da tangente, seno e cosseno de X radianos
#Por se calcular em radianos, é necessário a conversão do ângulo em graus para radianos
#A função que coverte os ângulos de grau para radianos é radians()
#A função que converte os ângulos de radianos para graus é degrees()

ang = int(input('Digite o valor do ângulo: '))

sinang = sin(radians(ang)) #Calula o seno (obtido em radianos) do angulo -> radians(ang) converte o valor de graus para radianos
cosang = cos(radians(ang)) #Calula o cosseno (obtido em radianos) do angulo -> radians(ang) converte o valor de graus para radianos
tanang = tan(radians(ang)) #Calula a tangente (obtido em radianos) do angulo -> radians(ang) converte o valor de graus para radianos

print(f'Valores de {ang}° \nSeno = {sinang:.2f} \nCosseno = {cosang:.2f} \nTangente = {tanang:.2f}')

