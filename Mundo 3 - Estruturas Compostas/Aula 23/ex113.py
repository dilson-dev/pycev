# Exercício Python #113 - Funções aprofundadas em Python

"""
DESAFIO 113
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
            # Havia colocado o método strip no input, porém a função int já valida e retira
            # os espaços de strings com números espaçadas.
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            # continue
            # Guanabara colocou o continue, mas é desnecessário.
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        # except Exception as erro:
        #     print(f'\033[1;31mERRO: {erro.__cause__}\033[m')
        else:
            return num


def leia_float(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.', 1))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        # except Exception as erro:
        #     print(f'\033[1;31mERRO: {erro.__cause__}\033[m')
        else:
            return num


# Programa Principal
n1 = leia_int('Digite um número Inteiro: ')
n2 = leia_float('Digite um número Real: ')

print(f'O valor Inteiro digitado foi {n1} e o Real foi {n2}')
