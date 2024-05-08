def moeda(value, coin):

    value = (f'{coin}{value:.2f}').replace('.', ',')
    return value


def aumentar(value, increase):

    return value + (increase*value/100)


def diminuir(value, depreciate):

    return value - (depreciate*value/100)


def dobro(value):

    return value*2


def metade(value):

    return value/2


