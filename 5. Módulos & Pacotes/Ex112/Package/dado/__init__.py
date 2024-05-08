def leiaDinheiro():

    while True: 

        value = input('Digite o preço: R$')

        analyse_value = value
        if ',' in analyse_value:

            analyse_value = analyse_value.replace(',', '')

        if '.' in analyse_value:

            analyse_value  = analyse_value.replace('.', '')

        if analyse_value.isnumeric() == False:

            print(f'\033[31mERRO: "{value}" é um preço invalido!\033[0;0;0m')
        
        else: 

            break

    
    if ',' in value:

        value = value.replace(',', '.')

    return float(value)