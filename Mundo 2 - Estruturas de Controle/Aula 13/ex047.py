# Exercício Python #047 - Contagem de pares

"""
DESAFIO 047
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""


'''
print()
for num in range(2, 51, 2):
    print(num, end='; ')
    """if num % 2 == 0:
    print(num)"""
print()
'''

# Em uma linha usando compreensão de listas:
[print(num, end=', ' if num != 50 else '.') for num in range(2, 51, 2)]
