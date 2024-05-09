def menu():


    
    print('='*30)
    while True:

        print('-'*30)
        print(('MENU PRINCIPAL').center(30))
        print('-'*30)
        print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
        print('\033[33m3\033[m - \033[34mSair do sistema\033[m')
        print('-'*30)

        user = None
        while True:

            try:

                user = int(input('\033[32mSua opção: \033[m'))

            except:

                print('\033[31mERRO! Digite um número inteiro válido.\033[m')

            else:

                if user != 1 and user != 2 and user != 3:

                    print('\033[31mERRO! Digite uma opção válida\033[m')

                else:

                    break

        if user == 1:

            print('-'*30)   
            print(('PESSOAS CADASTRADAS').center(30))
            print('-'*30)


        elif user == 2:

            print('-'*30)
            print(('NOVO CADASTRO').center(30))
            print('-'*30)

            
        elif user == 3: 

            print('='*30)
            break

menu()