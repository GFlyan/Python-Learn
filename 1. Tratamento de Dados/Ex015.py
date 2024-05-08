#Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qkmp = float(input('Quantos KM o veículo percorreu?'))

qda = float(input('Por quantos dias o veículo foi alugado?'))

preço_total = qda*60+qkmp*0.15

print(f'O preço total a ser pago pelo veículo é R${preço_total:.2f}, pois foi alugado por {qda:.0f} dias e rodou cerca de {qkmp:.0f}KM.')