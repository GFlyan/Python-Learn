#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

#Adequando à proposta

while True:

    user = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)

    if user < 0:

        break

    for n in range(0, 10):

        n += 1
        print(f'{user} x {n} = {user*n}')

    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')