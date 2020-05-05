# Exercício Python #046 - Contagem regressiva

"""
DESAFIO 046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
from emoji import emojize

print('\n\033[1;30mContagem regressiva para o estouro dos fogos de artíficio.\033[m\n')
for c in range(10, -1, -1):
    sleep(1), print(c)
print('\n\033[1;33mBOOM, POW, PA, PE, (...)!\033[1;35m', end='      ')
for r in range(10):
    print(emojize(':fireworks:       '), end='')
print()


# Soluções com temas diferentes de fogos de artifício:

# Foguete:
'''
print('\n\033[1;33mContagem regressiva para o lançamento do foguete:\n\033[m')

opcao = 0
for c in range(10, -1, -1):
    sleep(1), print(c)
print('\n\033[1;34mDecolando (...)!\033[m\n')

print(' ' * 10, emojize(':new_moon:'), '\n\n\n')
print(' ', emojize(':rocket:'))
'''

# Trem:
'''
print('\n\033[1;33mContagem regressiva para o trem partir:\n\033[m')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\n\033[1;34mPartindo (...)!\033[m', end='      ')

print(emojize(':suspension_railway:') * 20)
print(' ' * 20, '▔' * 22)
'''
