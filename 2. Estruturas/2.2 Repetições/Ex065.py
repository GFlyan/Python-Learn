#Crie um programa que leia vários números inteiros pelo teclado.
#Mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.


#Declarando variáveis

v0 = int(input(f'Digite um valor: ').strip())
user = input(f'Você quer continuar? ').strip().upper()
values = [v0]
somatory = v0
amount_values = 1

#Aplicando a sentença

while user != 'NAO':

    if user == 'SIM':

        value = int(input(f'Digite um valor: ').strip())
        user = input(f'Você quer continuar? ').strip().upper()
        values += [value]
        somatory += value
        amount_values += 1

    else:

        print('Opção invalida, tente novamente.')
        user = input(f'Você quer continuar? ').strip().upper()

#Mostrando resultados

media = somatory/amount_values
order_values = sorted(values)

if somatory == v0:

    print(f'Você digitou somente um valor, sendo impossível realizar a média pois são necessários 2 valores ou mais para realizar a média.')

else:

    print(f'A média entre os valores fornecidos é: {media}')
    print(f'O menor número fornecido foi o número {order_values[0]}\nE o maior número fornecido foi o número {order_values[-1]}')

