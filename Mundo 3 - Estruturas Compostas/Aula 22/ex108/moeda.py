from ex107.moeda import aumentar, diminuir, dobro, metade


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',', 1)
