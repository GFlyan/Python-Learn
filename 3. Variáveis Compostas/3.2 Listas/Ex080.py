#Crie um programa onde o usuário possa digitar cinco valores
#numéricos e cadastre-os em uma lista, já na posição
#correta de inserção (sem usar o sort()).

#No final, mostre a lista ordenada na tela.

'Definições'

values = []
count = 0

'Adequando à proposta'

for p in range(0, 5):

    while True:

        value = int(input(f'Digite um valor para a Posição {p}: '))

        if value in values:

            print('Valor duplicado... Não vou adicionar!')

        else:

            count += 1
            break

    if count == 1:

        values.insert(0, value)
        print(f'O valor {value} foi adicionado à posição 0!')

    elif count != 1:

        for c, v in enumerate(values):

            if c == 0 and value < v:

                values.insert(0, value)
                print(f'O valor {value} foi adicionado à posição 0!')
                break

            elif value > values[len(values)-1]:

                values.append(value)
                print(f'O valor {value} foi adicionado à posição {len(values)-1}!')
                break


            elif value > v and value < values[c+1]:

                values.insert(c+1, value)
                print(f'O valor {value} foi adicionado à posição {c+1}!')
                break

'Mostrando resultados'

print(f'Os valores digitados em ordem foram: {values}')

#28 linhas de codigo







