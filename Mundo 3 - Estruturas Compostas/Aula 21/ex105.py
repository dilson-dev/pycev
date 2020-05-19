# Exercício Python #105 - Analisando e gerando Dicionários

"""
DESAFIO 105
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:

- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).

Adicione também as docstrings da função.
"""


def notas(*ns, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    print('\n', '-' * 30, sep='')

    dicio = dict()

    dicio['total'] = len(ns)
    dicio['maior'] = max(ns)
    dicio['menor'] = min(ns)
    dicio['média'] = round(sum(ns) / len(ns), 3)

    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif dicio['média'] >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'

    return dicio


# Programa Principal
info = notas(3.5, 2, 6.5, 2, 7, 4)
print(info)
help(notas)
