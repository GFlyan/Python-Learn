#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações

#1. Quantidade de notas
#2. A maior nota
#3. A menor nota
#4. A média da turma 
#5. A situação (opcional)

#Adicione também as docstrings da função

def notas(*students_notes, sit=False):
    """
    -> A função student_notes tem funcionalidade de organizar em um dicionário a maior nota, menor nota, média das notas, quantidade de notas e até mesmo a situação da turma.
    :param students_notes: Recebe todas as notas dos alunos
    :param sit: Quando sit=True retorna a situação literal da média da turma
    :return: Retorna um dicionário contendo maior, menor, quantidade, média e situação de notas da turma
    """

    amount = minor = mayor = 0
    notas = dict()
    media = float()
    for c, n in enumerate(students_notes):

        media += n
        if c == 0:

            minor = mayor = n

        else:

            if n > mayor:

                mayor = n

            elif n < minor:

                minor = n

        amount = c+1

    media /= amount

    notas['Quantidade de Notas'] = amount
    notas['Maior Nota'] = mayor
    notas['Menor Nota'] = minor
    notas['Média'] = media

    if sit == True:

        if media < 5:

            notas['Situação'] = 'RUIM'

        if 5 <= media <= 7:
            
            notas['Situação'] = 'RAZOÁVEL'

        if media > 7:

            notas['Situação'] = 'BOA'


    return notas

'Mostrando Resultado'

notes = notas(7.0, 9, 10, 5.6, sit=True)
print(notes)