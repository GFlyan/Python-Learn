#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo:')
print('{} é:'.format(x))
print(type(x))
print('É numérico?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('É somente letra maiúscula?', x.isupper())
print('É somente letra minúscula?', x.islower())
print('É um espaço?', x.isspace())
print('É printável?',x.isprintable())

#type() mostra o tipo primitívo de um valor
#.isx() são funções chamadas de métodos de tipo, servem para verificar o tipo de um valor