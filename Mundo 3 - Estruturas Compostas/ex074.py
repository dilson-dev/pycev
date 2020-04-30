# Exercício Python #074 - Maior e menor valores em Tupla
"""
DESAFIO 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
# from random import sample

limitnums = int(input('\nDigite até qual número quer sortear: '))
quantnums = int(input('\nQuantos números quer sortear? '))

'''
nums = tuple(sample(range(limitnums + 1), quantnums))
print()
for num in nums:
    print(num, end=' ')
'''

nums = ()  # nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# maiornum = menornum = 0

print(f'\nValores sorteados:', end=' ')

for c in range(quantnums):
    nums += randint(0, limitnums),
    print(nums[c], end=' ')
    """
    if nums[c] > maiornum or c == 0:
        maiornum = nums[c]
    if nums[c] < menornum or c == 0:
        menornum = nums[c]
    """

print(f'\n\nMaior número: {max(nums)}.\nMenor número: {min(nums)}.')
