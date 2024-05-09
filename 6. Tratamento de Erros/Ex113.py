'''
Erros e Exceções

-> Os seguintes comandos podem ser utilizados para tratamento de erros/exceções em python

-> <try>: Vai tentar fazer algo.

-> <except>: Se <try> não conseguir realizar o código contido em seu bloco devido à um erro/exceção, o bloco <except> será executado.

-> <else>: Caso <try> não tenha nenhum problema, o bloco <else> poderá ser executado utilizando os retornos do bloco <try>.

-> <finally>: Este bloco será realizado independente do funcionamento ou não-funcionamento do bloco <try>, sendo o fechamento do programa.
'''

#Reescreva a função leiaInt() que foi feita no Ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido.

#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    
    while True:

        try:

            value = int(input('Digite um número inteiro: '))

        except KeyboardInterrupt:

            print(f'\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0        

        except:

            print(f'\033[31mERRO! Digite um valor inteiro válido.\033[m')

        else:

            return value
    

def leiaFloat():

    while True:

        try:

            value = float(input('Digite um número real: '))

        except KeyboardInterrupt:

            print(f'\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0

        except:

            print(f'\033[31mERRO! Digite um valor real válido.\033[m')

        else:

            return value


entire = leiaInt()
floating = leiaFloat()
print(f'O valor inteiro digitado foi {entire} e o real foi {floating}.')