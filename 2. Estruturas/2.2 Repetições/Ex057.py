#Laços de Repetição - Estrutura de Repetição com Teste Lógico

# Normalmente é utilizado em casos que não se possui um intervalo (x, y) para ser mediado por for
# while -> enquanto
# Tomar cuidado pois pode cair em um loop (laço de repetição) infinito

# Diferentemente do 'for', o 'while' é uma repetição que pode ser cessada (através de uma condição de parada)

#Faça um programa que leia o sexo de uma pessoas.
#O programa deverá aceitar somente os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = input(f'Você é HOMEM[H] ou MULHER[M]?').upper().strip()

while sex != 'H' and sex != 'M':

    print(f'Opção não aceita. Tente novamente:')
    sex = input(f'Você é HOMEM[H] ou MULHER[M]?').upper().strip()

if sex == 'H':

    print(f'MACHO!!!!')

else:

    print(f'MUIE!!!!')