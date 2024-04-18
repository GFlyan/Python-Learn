#Crie um programa onde o usuário digite uma expressão
#qualquer que use parênteses.

#Seu aplicativo deverá analisar se a expressão passada
#está com os parênteses abertos e fechados na ordem correta.

expression = input('Digite a expressão: ')
signs = ['+', '-', '*', '/']

count_opened_parentheses = 0
count_closed_parentheses = 0

amount_nums = 0
amount_digits = 0
correct = 0
incorrect = 0
start = 0
end_parenthese = None

for c, p in enumerate(expression):

    if p == '(':

        if ')' in expression[c:]: #Exemplo (6 * (2 - 3)

            start_parenthese = c



            if end_parenthese == None:

                end_parenthese = expression.rindex(')')

            else:

                end_parenthese = expression.rindex(')', c, end_parenthese)

            print(end_parenthese)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

            for n in expression[(start_parenthese+1):end_parenthese]:

                if n.isnumeric() == True:

                    amount_nums += 1

                if n.isdigit() == True and n.isnumeric == False:

                    amount_digits += 1

                if n == '(':

                    count_opened_parentheses += 1

                if n == ')':

                    count_closed_parentheses += 1

#----------------------------------------------------------------------------
            for s in signs:

                if (f'{s})') in expression:

                    incorrect += 1

            if count_closed_parentheses != count_opened_parentheses:

                incorrect += 1

            elif amount_nums == 1:

                incorrect += 1

            else:

                correct += 1
#--------------------------------------------------------------------------------

        else: # Exemplo: (3 + 4 * 2

            incorrect += 1

#--------------------------------------------------------------------------------

if incorrect >= 1:

    print('Os parenteses estão fechados em ordem incorretas.')

elif incorrect == 0:

    print('Os parênteses estão fechados em ordem correta.')