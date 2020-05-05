# Exercício Python #017 - Catetos e Hipotenusa

"""
DESAFIO 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
|\
| \
|  \
|x__\
"""

from math import hypot
co = float(input('\033[1;30mComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('\nA hipotenusa medirá {}{:.2f}{}.'.format(
    '\033[1;35m', h, '\033[1;30m'))
