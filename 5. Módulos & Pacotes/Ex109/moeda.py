def moeda(value, coin='R$'):

    value = (f'{coin}{value:.2f}').replace('.', ',')
    return value


def aumentar(value, increase, format=False):

    value = value + (increase*value/100)
    return value if format == False else moeda(value=value)


def diminuir(value, depreciate, format=False):

    value = value - (depreciate*value/100)
    return value if format == False else moeda(value=value)


def dobro(value, format=False):

    value *= 2
    return value if format == False else moeda(value=value)


def metade(value, format=False):

    value /= 2
    return value if format == False else moeda(value=value)


