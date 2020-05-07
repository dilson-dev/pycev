# Exercício Python #091 - Jogo de Dados em Python

"""
DESAFIO 091
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

# Com compreensão de dicionários:
# jogadores = {f'jogador {num}': randint(1, 6) for num in range(1, 5)}

for k, v in jogadores.items():
    print(f'\n{k} jogou o dado...')
    sleep(1)
    print(f'{k} tirou {v}.')
    sleep(1)

# Usando expressão lambda (Expressões lambdas são usadas para definir funções sem atribui-las)
# ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# O parâmetro key recebe uma função que determina quais valores serão usados para ordenação.
# Esses valores são por padrão o índice 0 de um conjunto, ou os próprios valores, caso não existam conjuntos

# Para ordenar os valores dos dicionários é preciso passar uma função para este parâmetro , para definir
# o índice 1, pois como as chaves estão no índice 0 é elas que ele pega.

# Assim precisamos usar a função itemgetter do package operator para fazer isso.

# itemgetter(0) pega as chaves, e itemgetter(1) pega os valores, pois dicionário.items() retorna:
# [(chave, valor), (chave, valor), (chave, valor)], e assim por diante, conforme o tamanho do dicionário.

# Ao final a variável ranking fica da seguinte forma, onde N é o número do jogador, e pontos é sua pontuação
# E como os pontos estão no índice 1, é por estes que é ordenado a variável ranking:
# ranking = [('jogadorN', pontos), ('jogadorN', pontos), ('jogadorN', pontos), ('jogadorN', pontos)]

# Por exemplo: [('jogador3', 5), ('jogador1', 3), ('jogador4', 1), ('jogador2', 1)]

print(), print('-' * 32)
print(f'| {"Ranking dos jogadores":^28} |')
print('-' * 32)
print(f'| Posição |  Jogador  | Pontos |')
print('-' * 32)


# Posições diferentes para pontuações iguais:
'''
for pos, (k, v) in enumerate(ranking, 1):  # for pos, tup in enumerate(ranking, 1):
    sleep(1)
    print(f'| {str(pos) + "º":^7} | {k:^9} | {v:^6} |')  # print(f'| {str(pos) + "º":^7} | {tup[0]:^9} | {tup[1]:^6} |')
'''

# Posições iguais para pontuações iguais:
posicao = 1
for num in range(len(ranking)):
    if num == 0 or ranking[num][1] == ranking[num - 1][1]:
        print(f'| {str(posicao) + "º":^7} | {ranking[num][0]:^9} | {ranking[num][1]:^6} |')
    else:
        posicao += 1
        print(f'| {str(posicao) + "º":^7} | {ranking[num][0]:^9} | {ranking[num][1]:^6} |')

print('-' * 32)
