# Refaça o Ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

# 1° Tratamento de dados sobre os valores informados do comprimento das retas

comprimentos = input('Digite o comprimento das retas:').strip()
r1, r2, r3 = comprimentos.split()
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)
lados = [r1, r2, r3]

# 2° Condição de existência de um triângulo

if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:

    triângulo = True

else:

    triângulo = False

# 3° Tipos de triângulo

if triângulo == True:

    if r1 == r2 and r1 == r3:

        print('Será formado um triângulo equilátero.')

    elif r1 == r2 and r1 != r3:

        print('Será formado um triângulo isósceles.')

    elif r2 == r3 and r2 != r1:

        print('Será formado um triângulo isósceles.')

    elif r3 == r1 and r3 != r2:

        print('Será formado um triângulo isósceles.')

    else:

        print('Será formado um triângulo escaleno.')

else:

    print('Não é possível formar um triângulo.')