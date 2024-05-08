# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1, n2, n3 = input('Digite três números:').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:

    if n2 > n3:

        print(f'O maior número é {n1} e o menor {n3}.')

    else:

        print(f'O maior número é {n1} e o menor {n2}.')

elif n2 > n1 and n2 > n3:

    if n1 > n3:

        print(f'O maior número é {n2} e o menor {n3}.')

    else:

        print(f'O maior número é {n2} e o menor {n1}.')

else:

    if n1 > n2:

        print(f'O maior número é {n3} e o menor {n2}.')

    else:

        print(f'O maior número é {n3} e o menor {n1}.')