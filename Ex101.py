'''
Interactive Help 

-> É utilizado para saber como utilizar uma função
-> help(x) ou print(x.__doc__)

Docstrings

-> É a documentação que deve ser posta em uma função
-> Para criar a documentação(docstring) deve-se utilizar 3 áspas duplas (""")
   no incio e no fim.

Parâmetros Opcionais

-> Uma função pode ser definida com parâmetros opcionais:

    def function (x, y=z)

    Na função function, x é um parâmetro obrigatório e y é um parâmetro opcional que
    se caso y não seja fornecido quando a função for utilizada, ele irá receber o valor
    z.

-> Para definição de um parâmetro opcional deve-se utilizar <param>=...

Escopo de Variáveis

Variável Local -> Uma variável local existe somente dentro de uma função

Variável Global -> Uma variável global existe fora e dentro de uma função (ou seja, 
                   em todas as ocasiões possíveis de utilização para a mesma)

Retornando Valores

return <...> -> O return é utilizado para retornar algo, podendo ser qualquer tipo de valor
                ou variável, desde que estabelecido na função.
'''

#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

'Adequando à Propósta'

def voto(year_born):
    """
    -> A função voto retorna um valor que indica a possibilidade de voto de um indivíduo se baseando no ano de nascimento do mesmo, sendo que o ano de nascimento deve ser passado como parâmetro.

    <param: year_born> -> Recebe o ano de nascimento
    """

    from datetime import datetime
    age = datetime.now().year - year_born

    if age < 16:

        return f'Com {age} anos: VOTO NEGADO'
    
    elif 16 <= age <= 17 or age > 70:

        return f'Com {age} anos: VOTO OPCIONAL'
    
    elif 18 <= age <= 70:

        return f'Com {age} anos: VOTO OBRIGATÓRIO'


'Mostrando Resultado'

print('-'*30)
year = int(input('Em que ano você nasceu? '))
print(voto(year_born=year))



















