# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

# 1° Tratamento de dados sobre as notas fornecidas

nota1, nota2 = input('Digite suas notas:').split()
nota1 = float(nota1)
nota2 = float(nota2)

# 2° Informações sobre a média obtida

média = float((nota1 + nota2) / 2)

if média < 5.0:

    print('REPROVADO')

elif média >= 5.0 and média < 7:

    print('RECUPERAÇÃO')

else:

    print('APROVADO')