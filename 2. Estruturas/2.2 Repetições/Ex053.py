# Crie um programa que leia uma frase qualquer e diga:
# Se ela é um palíndromo, desconsiderando os espaços

# Apos a Sopa
# O lobo ama o bolo

#Definindo o armazenador da frase final

reversed_phrase = ''

#Fornecendo a frase a ser analisada

phrase = str(input('Escreva uma frase para saber se ela forma um palíndromo: ').strip()).upper()
phrase = phrase.replace(' ', '') #Ignorando os espaços

total_letters = len(phrase)

#Escrevendo a frase ao contrário

for letter in range(0, total_letters):

    reversed_letter = (total_letters-1) - letter
    reversed_phrase += phrase[reversed_letter]

#Verificando a existência do palíndromo

if phrase == reversed_phrase:

    print(f'A frase escolhida é um palíndromo.')

else:

    print(f'A frase escolhida não é um palíndromo.')