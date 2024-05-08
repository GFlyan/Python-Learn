def moeda(value=0, coin='R$'):

    value = (f'{coin}{value:.2f}').replace('.', ',')
    return value


def aumentar(value=0, increase=0, format=False):

    value = value + (increase*value/100)
    return value if format == False else moeda(value=value)


def diminuir(value=0, depreciate=0, format=False):

    value = value - (depreciate*value/100)
    return value if format == False else moeda(value=value)


def dobro(value=0, format=False):

    value *= 2
    return value if format == False else moeda(value=value)


def metade(value=0, format=False):

    value /= 2
    return value if format == False else moeda(value=value)


def resumo(value=0, increase=0, depreciate=0):
    
    print('-'*30)
    print(('RESUMO DO VALOR').center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(value)}')
    print(f'Dobro do preço: \t{dobro(value=value, format=True)}')
    print(f'Metade do preço: \t{metade(value=value, format=True)}')
    print(f'{increase}% de aumento: \t{aumentar(value=value, increase=increase, format=True)}')
    print(f'{depreciate}% de redução: \t{diminuir(value=value, depreciate=depreciate, format=True)}')
    print('-'*30)
