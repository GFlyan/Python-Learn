#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

'Adequando à Propósta'

def leiaInt(show):
    """ 
    -> A função leiaInt serve para validar se o valor informado é um valor inteiro.

    :param show: Um parâmetro que tem função de input
    :return: Retorna o valor em forma de inteiro 
    """

    while True:

        value = input(show)
        if value.isnumeric() == True:
            
            break

        else:
        
            print('\033[31mERRO! Digite um número inteiro válido.\033[37m')

    return value


'Mostrando Resultado'

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')