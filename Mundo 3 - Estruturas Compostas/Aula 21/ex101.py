# Exercício Python #101 - Funções para votação

"""
DESAFIO 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

from datetime import datetime


def voto(nasc):
    """
    Calcula a condição de voto a partir do ano de nascimento de uma pessoa.

    :param nasc: Ano de nascimento da pessoa
    """
    ano = datetime.now().year
    idade = ano - nasc

    if idade < 16:
        cond = 'NEGADO'
    elif idade <= 17 or idade >= 65:
        cond = 'OPCIONAL'
    else:
        cond = 'OBRIGATÓRIO'

    # return r
    return f'Com {idade} anos: VOTO {cond}.'


# Programa Principal
print('\n', '-' * 30, sep='')
nascimento = int(input('Ano de nascimento: '))

print(voto(nascimento), end='\n\n')
help(voto)

# Escopo de importação
