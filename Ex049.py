# Refaça o Ex009, mostrando a tabuada de um número que o usuário escolher
# Entretanto agora utilizando o laço for

#Escolha do número a ser utilizado para saber sua tabuada

multiplicando = int(input('Escolha um número para saber sua tabuada do 0 a 10: '))

#Tabuada utilizando o for
print(f'''{'TABUADA':-^40}''')
for numero in range(0,10):

    multiplicador = numero+1
    print(f'{multiplicando}x{multiplicador} = {multiplicando*multiplicador}')

print(f'-'*40)