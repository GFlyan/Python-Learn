#Crie dentro do pacote um módulo chamado dado, depois crie uma função chamada leiaDinheiro que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitas apenas valores que sejam monetários.

from Package import dado
from Package import moeda

value = dado.leiaDinheiro()
moeda.resumo(value=value)