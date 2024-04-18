#Faça um programa que leia quanto dinheiro uma pesoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere: U$1,00 = R$3,27

din = float(input('Quantos reais você tem na sua carteira? R$'))

dol = din/3.27

print(f'Se você quiser comprar uma quantia em dólares com seus {din} reais, você irá conseguir {dol:.2f} dólares!')
