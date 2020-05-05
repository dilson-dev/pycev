#

"""
DESAFIO 091
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep


def take_second(elem):
    return elem[1]


jogadores = {input(f'\nNome do jogador {i}: '): randint(1, 6) for i in range(1, 5)}

for j, v in jogadores.items():
    print(f'\n{j} jogou o dado...')
    sleep(randint(2, 4))
    print(f'{j} tirou {v}.')
    sleep(3)

jogadores = {j: v for j, v in sorted(jogadores.items(), key=take_second, reverse=True)}
# key=lambda item: item[1]

c = 1
print('\nRanking dos jogadores: \n')
for j, v in jogadores.items():
    print(f'{c}º lugar: {j} com {v}.')
    c += 1

# for j in jogadores.keys():
#     if jogadores[j] == valores[-1]:
#         print(f'\n{j} tirou o maior valor no dado, e é o vencedor, ou um dos vencedores.')
