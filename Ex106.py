#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.

#Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#OBS: Use cores.


def PyHelp():
    """
    -> PyHelp tem funcionalidade de fornecer informações sobre funções.
    :return: Não possui retorno
    """
    from time import sleep

    while True:
        
        print('\033[30;42m~'*(len('SISTEMA DE AJUDA PyHelp')+4))
        print('  SISTEMA DE AJUDA PyHelp  ')
        print('~'*(len('SISTEMA DE AJUDA PyHelp')+4))
        function = input('\033[0;0mFunção ou Biblioteca> ')

        if function == 'FIM':

            print('\033[30;41mFINALIZANDO...\33[0;0m')
            break

        print('\033[30;44m~'*(len(f"Acessando o manual do comando '{function}'")+4))
        print(f"  Acessando o manual do comando  '{function}'  ")
        print('~'*(len(f"Acessando o manual do comando '{function}'")+4))

        sleep(1.5)
        print('\033[47;30m')
        help_function =  help(function)

PyHelp()
    
