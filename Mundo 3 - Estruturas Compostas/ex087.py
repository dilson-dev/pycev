# Exercício Python #087 - Mais sobre Matriz em Python
"""
DESAFIO 087
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valroes pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.
"""

'''#       0  1  2
matriz = [[1, 2, 3], # 0
          [4, 5, 6], # 1
          [7, 8, 9]] # 2

# matriz[Linha][Coluna]

'''

matriz = [[], [], []]
somapar = somacol3 = 0  # mai
# print()
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para {[linha, coluna]}: ')))
        if matriz[linha][coluna] % 2 == 0:  # matriz[linha][-1]
            somapar += matriz[linha][coluna]
    somacol3 += matriz[linha][2]
print('=-' * 35)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='' if coluna != 2 else '\n')
print('=-' * 35)
print(f'Soma dos pares: {somapar}.')
print(f'Soma valores da terceira coluna: {somacol3}.')
print(f'Maior valor da segunda linha: {max(matriz[1])}.')

'''
for linha in range(3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}.')

for coluna in range(3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}.')
'''
