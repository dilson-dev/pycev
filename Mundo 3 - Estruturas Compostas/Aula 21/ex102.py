# Exercício Python #102 - Função para Fatorial

"""
DESAFIO 102
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('\n', '-' * 30, sep='')
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end=' x ' if cont != 1 else ' = ')
        f *= cont
    return f


# Programa Principal
print(fatorial(5, show=True))
print(fatorial(3, True))
print(fatorial(10))
help(fatorial)
