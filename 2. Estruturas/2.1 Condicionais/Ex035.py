# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.


# 1° Tratamento dos dados fornecidos

r1, r2, r3 = (input('Digite o valor do comprimento das três retas:').strip()).split()
r1 = float(r1)
r2 = float(r2)
r3 = float(r3)

# 2° Condição de formação de um triângulo

if r1 < (r2+r3):

    possibilidadeR1 = True

else:

    possibilidadeR1 = False

if r2 < (r1+r3):

    possibilidadeR2 = True

else:

    possibilidadeR2 = False

if r3 < (r1+r2):

    possibilidadeR3 = True

else:

    possibilidadeR3 = False

# 3° Possibilidade de formar ou não um triângulo

if possibilidadeR1 and possibilidadeR2 and possibilidadeR3 == True:

    print(f'As retas podem formar um triângulo!')

else:

    print(f'As retas não podem formar um triângulo.')


