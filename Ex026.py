# Faça um programa que leia uma frase pelo teclado e mostre:

    # Quantas vezes aparece a letra "A"
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').strip()
letra_A = frase.upper().count('A')

print(f'A letra "A" aparece {letra_A} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição: {frase.upper().find("A")}')
print(f'A letra "A" aparece pela última vez na posição: {frase.upper().rfind("A")}')