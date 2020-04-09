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
totpares = soma3coluna = 0
print()
for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite um valor para {[linha, coluna]}: ')))
        if matriz[linha][coluna] % 2 == 0:  # matriz[linha][-1]
            totpares += matriz[linha][coluna]
    soma3coluna += matriz[linha][2]
print('=-' * 35)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('=-' * 35)
print(f'Soma dos pares: {totpares}.')
print(f'Soma valores da terceira coluna: {soma3coluna}.')
print(f'Maior valor da segunda linha: {max(matriz[1])}.')
