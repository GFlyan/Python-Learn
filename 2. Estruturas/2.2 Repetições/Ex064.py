#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada
#No final mostre quantos números foram digitados e qual foi a soma entre eles
#Desconsiderando o flag

#Declaração de variáveis

value = 0
amount_value = 0
somatory = 0

#Adequando a sentença

while value != 999:

    value = int(input(f'Digite um valor: ').strip())

    if value != 999:

        amount_value += 1
        somatory += value

#Mostrando resultado

print(f'''{'Foi digitado' if amount_value == 1 else 'Foram digitados'} {amount_value} {'valor' if amount_value == 1 else 'valores'}.''')

if amount_value == 1:

    print(f'A soma é o próprio valor fornecido: {somatory}')

else:

    print(f'''A soma entre os valores fornecidos é: {somatory}''')
