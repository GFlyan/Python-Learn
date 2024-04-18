# Escreva um programa que leia a velocidade de um carro.

# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

# A multa vai custar R$7,00 por cada Km acima do limite.

# 1° Tratamento de dados sobre a velocidade fornecida

velocidade = input('Qual era sua velocidade?').strip()

if ('Km/h' in velocidade) == True:

    velocidade = velocidade.split('Km/h')
    velocidade = velocidade[0]

velocidade = int(velocidade)

# 2° Análise da velocidade

if velocidade > 80:

    velocidade_acima = velocidade - 80
    valor_multa = velocidade_acima*7
    print(f'Você estava {velocidade_acima}Km/h acima do limite permitido pela via!\nSua multa será de R${float(valor_multa):.2f}!')

else:

    print(f'Você não estava acima do limite permitido pela via.')

