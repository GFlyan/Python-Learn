#Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

payment = float(input('Qual o seu salário mensal? R$'))

buff_payment = payment*15/100

new_pay = payment+buff_payment

print(f'Seu novo salário terá um acrescimo de 15%, você irá ganhar R${new_pay:.2f}!')
