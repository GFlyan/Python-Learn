#Crie um programa que tenha uma tupla com vária palavras (não usar acentos)
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'Definições'

words = ('Maça',
        'Aviao',
        'Guitarra',
        'Chocolate',
        'Cachorro',
        'Lua',
        'Bicicleta',
        'Piano',
        'Montanha',
        'Caneta')

'Adequando à proposta'

for word in words:

    print(f'Na palavra {word.upper()} temos as seguintes vogais:', end=' ')

    vowels = ''
    for letter in word:

        if letter.upper() == 'A' or letter.upper() == 'E' or letter.upper() == 'I' or letter.upper() == 'O' or letter.upper() == 'U':

            vowels += (f'{letter.upper()} ')

    print(vowels)
