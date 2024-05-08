#Faça um programa que leia as notas de um aluno, calcule-as, mostre a sua média e mostre uma mensagem de aprovação/reprovação
#Nota de corte é de 5, abaixo disso o aluno estará reprovado


p1 = float(input('Nota da primeira prova: '))
p2 = float(input('Nota da segunda prova: '))
p3 = float(input('Nota da terceira prova: '))

midp = ((p1+p2+p3)/3)

print(f'Sua média é: {midp:.1f}')

if midp >= 5:
    print('Parabéns você foi aprovado!')
elif midp < 5:
    print('Você foi reprovado.')




