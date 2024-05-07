 #Crie um programa que tenha uma função fatorial() que receba dois parâmetros que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

'Adequando à Propósta'

def fatorial(num, show=False):
    """
    -> A função fatorial calcula o fatorial do dado parâmetro.

    :param num: Parâmetro que recebe o número que será calculado o fatorial
    :param show: Parâmetro que define se aparecerá ou não as operações realizadas para calcular o fatorial
    :param return: Retorna o fatorial do número fornecido
    """

    fat = 1
    while num != 0:
            
        fat *= num
        num -= 1
        if show == True:

            print(f'{num+1}', end='')

            if num != 0:

                print(' x ', end='')

            else:
                
                print(f' = ', end='')        
                
    return fat

'Mostrando Resultado'

value = int(input('Digite um valor para saber seu fatorial: '))
print(fatorial(value, True))

