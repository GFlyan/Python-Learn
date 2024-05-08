#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

largura = float(input('Qual a largura da parede em metros?'))
altura =  float(input('Qual a altura da parede em metros?'))

area = largura*altura

#Área é dada em m²

#Lembrando que uma 1l de tinta pinta 2m²
tinta_area = area/2

print(f'Você irá precisar de {tinta_area} litros de tinta para pintar sua parede.')
