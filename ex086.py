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

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'\nDigite um valor para {[linha, coluna]}: ')))

print('=-' * 35)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# print(sum(matriz[2]))
