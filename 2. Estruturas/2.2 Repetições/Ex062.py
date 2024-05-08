#Melhore o Ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos
#Equação PA ->  an = a1+(n-1)*r

#Declarando variáveis utilizáveis

terms = []
n = 1 #Acumulador, representa o primeiro índice de primeiro termo da PA
an = 0 #Termo geral vazio

#Informações fornecidas pelo usuário

a1 = int(input(f'Insira o primeiro termo da PA: ').strip())
r = int(input(f'Insira o valor da razão da PA: ').strip())

#Adequando PA ao while

while an != (a1+(10-1)*r):

    an = (a1+(n-1)*r)
    terms += [an]
    n += 1

#Mostrando o resultado

print(f'Os dez primeiros termos da PA formada com os dados fornecidos são: {terms}')
user = input(f'Gostaria de ver mais termos dessa PA? ').strip().upper()

if user == 'SIM': #Solicitando novos termos

    new_terms = []

    amount_terms = int(input(f'Digite a quantidade de novos termos que você gostaria de ver: '))

    while amount_terms != 0:

        an = (a1+(n-1)*r)
        amount_terms -= 1
        n += 1
        new_terms += [an]

    print(f'Esses são os novos termos solicitados: {new_terms} ')

elif user == 'NAO': #Finalizando o programa

    print(f'OK')

