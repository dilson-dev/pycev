# Exercício Python #104 - Validando entrada de dados em Python

"""
DESAFIO 104
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n')
"""


def leiaInt(texto=''):
    print('\n', '-' * 30, sep='')
    while True:
        num = input(texto)
        if num.isnumeric():
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
