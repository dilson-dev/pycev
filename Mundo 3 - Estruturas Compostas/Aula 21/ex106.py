# Exercício Python #106 - Sistema interativo de ajuda em Python
# Python exercise #106 - Interactive helping system in Python

"""
DESAFIO 106
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
"""
from time import sleep


def escrever(text='', cor=''):
    tam = len(text) + 6
    print(end=cor)
    print('~' * tam)
    print(f'|  {text}  |')
    print('~' * tam)
    print(end='\033[m')


def ajuda(func):
    escrever(f'Acessando o manual do comando \'{função}\'', cor='\033[1;44m')
    sleep(1)
    print('\033[7m')
    help(func)
    print(end='\033[m')
    sleep(1)


# Programa Principal
while True:
    escrever('SISTEMA DE AJUDA PyHELP', cor='\033[1;42m')
    função = input('Função ou Biblioteca > ')
    if função.upper() == 'FIM':
        break
    ajuda(função)

escrever('ATÉ LOGO!', cor='\033[1;41m')
