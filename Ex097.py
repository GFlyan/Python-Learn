#Faça um programa que tenha uma função chamada escreva().
#A função receberá um texto qualquer como parâmetro e mostrará uma mensagem com tamanho adaptável.

#Exemplo:

#-------------
# Olá, mundo!
#-------------

'Adequando à proposta'

def escreva(text):

    print('-'*len(text))
    print(f'{text}')
    print('-'*len(text))

'Mostrando resultados'

text = input('Digite algo: ').upper()
escreva(text=text)