'''
Funções

-> Funções são rotinas criadas para serem utilizadas a qualquer momento, abrange um conjunto de código trabalhoso
que normalmente você utiliza diversas vezes, e para polpar trabalho criamos uma função com a mesma utilidade.

-> Para criar uma função utilizamos def <função>():

-> Os parênteses podem receber ou não parâmetros def <função>(par)

-> Os parâmetros podem ser variáveis ou dados como strings 

    -> <função>(par) - variável
    -> <função>('par') - string

-> A função pode receber diversos parâmetros, desde que estejam definidos nos parentêses
na hora da definição da função

-> É possível explicitar, na hora de utilizar uma função criada, sendo capaz assim de fugir do padrão
pré definido da função, entretanto quando não forem explicitados os parâmetros, a função irá agir de
acordo com a ordem definida

-> Quando não se tem uma quantidade específica de parâmetros que serão recebidos, utiliza-se 
def <função>(*par), onde os parâmetros serão guardados em uma tupla

'''

#Faça um programa que tenha uma função chamada área().
#A função deverá receber as dimensões de um terreno retangular (largura, comprimento) e mostre a área do terreno.

'Adequando à proposta'

def área(largura, comprimento):

    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m².')

print('-'*30)
print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

'Mostrando resultados'

área(largura=largura, comprimento=comprimento)
