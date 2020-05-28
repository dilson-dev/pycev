# Exercício Python #104 - Validando entrada de dados em Python

"""
DESAFIO 104
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um nº: ')
"""


def leiaInt(msg=''):
    """
    -> Valida entradas numéricas do tipo inteiro.
    :param msg: (opcional) Mensagem que será exibida na tela para entrada do valor numérico.
    :return: O valor numérico recebido como caracter transformado em inteiro.
    """
    print('\n', '-' * 30, sep='')
    while True:
        num = input(msg).strip()
        if num.replace('-', '', 1).isdigit():  # isnumeric()
            return int(num)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        # print(f'\033[1;31mERRO! Valor "{num}" inválido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
