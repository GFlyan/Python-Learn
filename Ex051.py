# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# Equação de uma PA: an = a1+(n-1)*r


#Definição da lista de termos

termos = []

#Lendo o primeiro termo e a termo razão

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

#Desenvolvendo a PA para os 10 primeiros termos e armazenando resultados

for n in range(0, 10):

    n += 1
    an = a1+(n-1)*r
    termos += [an]

#Mostrando os resultados

print(f'Os 10 primeiros termos da PA são: {termos}')


