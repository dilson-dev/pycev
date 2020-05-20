# Exercício Python #103 - Ficha do Jogador

"""
DESAFIO 103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""


def ficha(jog='<desconhecido>', gol=0):
    """
    -> Mostra a ficha de um jogador, o nome e a quantidade de gols no campeonato.
    :param nome: (opcional, valor padrão <desconhecido>) Nome do jogador.
    :param gols: (opcional, valor padrão 0) Quantidade de gols que o jogador fez.
    :return: Sem retorno.
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
print('\n', '-' * 30, sep='')

nome = input('Nome do Jogador: ').strip()
gols = input('Número de Gols: ').strip()

gols = int(gols) if gols.isnumeric() else 0

if nome:
    ficha(nome, gols)
else:
    ficha(gol=gols)
