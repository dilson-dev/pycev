matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Posição {[linha, coluna]}: '))
# print(v for v in lista for lista in matriz)
[print(f'{" | ".join(str(v) for v in lista)}') for lista in matriz]
