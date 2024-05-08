#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência

#No final, mostre uma listagem de preços, organizando os dados de forma tabular.

'Definições'

products = ('Caneta', '1,50', 'Lápis', '2,00')

'Adequação à proposta'

print('-='*20)
print(f'''{'LISTAGEM DE PREÇOS':^40}''')
print('-='*20)

count = 1
for p in products[::2]:

    print(f'''{p:-<33}R$ {products[count]}''')
    count += 2

