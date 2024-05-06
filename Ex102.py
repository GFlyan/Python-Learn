#Crie um programa que tenha uma função fatorial() que receba dois parâmetros que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):

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

value = int(input('Digite um valor para saber seu fatorial: '))
print(fatorial(value, True))

