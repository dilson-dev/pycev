# Exercício Python #086 - Matriz em Python
"""
DESAFIO 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
   _ _ _
0 |_|_|_|
1 |_|_|_|
2 |_|_|_|
   0 1 2

No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[], [], []]

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for de alimentação (colocar valores dentro da matriz)
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'\nDigite um valor para {[linha, coluna]}: ')))
        # matriz[linha][coluna] = int(input(f'\nDigite um valor para {[l, c]}: '))  # f'[{l}, {c}]:'
print('-=' * 35)
# for de impressão (mostrar valores na tela)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='' if coluna != 2 else '\n')

'''  # Perguntando as dimensões da matriz
linhas = int(input('\nQuantas linhas? '))
colunas = int(input('Quantas colunas? '))
matriz = [[0] * colunas for linha in range(linhas)]
# matriz = [[] for linha in range(linhas)]
for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = int(input(f'\nDigite um valor para {[linha, coluna]}: '))
        # matriz[linha].append(int(input(f'\nDigite um valor para {[linha, coluna]}: ')))
print('-=' * 35)
for linha in range(linhas):
    for coluna in range(colunas):
        print(f'[{matriz[linha][coluna]:^5}]', end='' if coluna != colunas - 1 else '\n')
'''
'''
linhas = int(input('\nQuantas linhas? '))
colunas = int(input('Quantas colunas? '))
matriz = [[0] * colunas for linha in range(linhas)]
for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = int(input(f'\nDigite um valor para {[linha + 1, coluna + 1]}: '))
print('-=' * 35)
for linha in range(linhas):
    for coluna in range(colunas):
        print(f'[{matriz[linha][coluna]:^5}]', end='' if coluna != colunas - 1 else '\n')
'''
