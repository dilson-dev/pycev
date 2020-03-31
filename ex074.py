"""
DESAFIO 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

nums = ()
maiornum = menornum = 0

print(f'\nValores sorteados:', end=' ')

for c in range(5):
    nums += randint(0, 10),
    print(nums[c], end=' ')
    if nums[c] > maiornum or c == 0:
        maiornum = nums[c]
    if nums[c] < menornum or c == 0:
        menornum = nums[c]

'''
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
'''

print(f'\n\nMaior número: {maiornum}.')
print(f'Menor número: {menornum}.')
