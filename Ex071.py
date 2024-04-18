#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado e o programa vai informar quantas cédulas de cada valor será entregue.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#Definições

bank = [50, 20, 10, 1]

print('='*30)
print(f'''{'BANCO DO FLY':^30}''')
print('='*30)

#Adequação à proposta

value = int(input('Qual valor você quer sacar? R$').strip())

while True:

    for i in bank:

        banknotes = value // i
        value = value % i

        if banknotes != 0:

            print(f'Total de {banknotes} cédulas de R${i}')

        if value == 0:

            break

    break

print('='*30)
print('Volte sempre ao BANCO DO FLY! Tenha um bom dia!')