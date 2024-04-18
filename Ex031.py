# Desenvolva um programa que pergunte a distância de uma viagem em Km.

# Calcule o preço da passagem cobrando R$0,50 por Km para viagen de até 200Km e R$0,45 para viagens mais longas.


# 1° Tratamento de dados sobre a distância da viagem

distância_viagem = str(input('Qual a distância da viagem?')).strip()

if ('Km' in distância_viagem) == True:

    distância_viagem = distância_viagem.split('Km')
    distância_viagem = distância_viagem[0]

distância_viagem = int(distância_viagem)

# 2° Cálculo do preço da viagem

if distância_viagem > 200:

    valor_viagem = distância_viagem*0.45
    print(f'O valor da viagem será de R${valor_viagem:.2f}!')

else:

    valor_viagem = distância_viagem*0.50
    print(f'O valor da viagem será de R${valor_viagem:.2f}!')