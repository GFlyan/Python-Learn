#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.

#Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#OBS: Use cores.


def interactive_help():
    """
    -> interactive_help tem funcionalidade de fornecer informações sobre funções.
    :return: Não possui retorno
    """
    
    while True:
        
        print('*'*30)
        function = input('Digite a função que você deseja saber as informações: ')
        print('-='*15, '\n')
        help_function =  help(function)
        print('-='*15)

        user = None
        while user != 'CONTINUAR' and user != 'FIM':

            user = input('[CONTINUAR/FIM] ').upper()

        if user == 'FIM':

            break

interactive_help()
    
