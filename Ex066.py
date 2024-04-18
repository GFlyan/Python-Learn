#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada (break).
#No final, mostre quantos números foram digitados e qual foi a soma entre eles.
#(desconsiderando o flag)

#Definições

amount_values = 0
somatory = 0

#Adequando à proposta

while True:

    user = int(input(f'Digite um valor (999 para parar): ').strip())

    if user == 999:

        break

    amount_values += 1
    somatory += user

print(f'A soma dos {amount_values} foi {somatory}!')
