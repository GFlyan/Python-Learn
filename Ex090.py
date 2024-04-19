#Variáveis Compostas - Dicionários

#Dicionários sao variáveis compostas que armazenam dados de forma semelhante à listas e tuplas,
#entretanto suas posições referênciais são diferentes, sendo que em listas/tuplas
#as posições são referênciais númericos, nos dicionários as posições são referênciais
#literais.

#Podem ser representados por dict() ou {}

##Values (valores) -> <dict>.values()

#É o valor atribuido à uma posição literal

##Keys (chaves) -> <dict>.keys()

#São as próprias posições literais

##Items (itens) -> <dict>.items()

#É o conjunto das chaves e valores

##Adicionando elementos em um dicionário

#Para adicionar posições literais(keys) e valores em um dicionário, não utilizamos nenhuma função
#diferentemente das listas.

#Utilizamos a seguinte sintaxe:

#<dict>["<position">] = value

###Para evitar relações/conexões durante atribuições utilizamos o método 
#copy -> <dict>.copy(), sendo que em listas podemos utilizar slices [:] e
#o método copy.

#Faça um programa que leia nome e média de um aluno, guardando também 
#a situação em um dicionário.

#No final, mostre o conteúdo da estrutura na tela.

'Definições'

person = dict()

'Adequando à proposta'

person['nome'] = input('Digite seu nome: ')
person['média'] = float(input(f'Média de {person["nome"]}: '))
            
'Mostrando respostas'
    
print('-='*15)
print(f'Nome é igual a {person["nome"]}')
print(f'Média é igual a {person["média"]}')
print(f'Situação: ', end='')

if person['média'] < 5:

    print('REPROVADO')

else:

    print('APROVADO')


