# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada

"""
DESAFIO 006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# from math import sqrt
cores = {'bf': '\033[1;30m',
         'ru': '\033[4;35m',
         'amf': '\033[1;33m',
         'vmf': '\033[1;31m',
         'vdf': '\033[1;32m',
         'l': '\033[m'}

n = int(input('\n{}Digite um número: {}'.format(cores['bf'], cores['l'])))
print('\nO dobro de {}{}{} é {}{}{}.'.format(
    cores['ru'], n, cores['l'], cores['amf'], (n * 2), cores['l']))
print('O triplo de {}{}{} é {}{}{}.'.format(
    cores['ru'], n, cores['l'], cores['vmf'], (n * 3), cores['l']))
print('A raiz quadrada de {}{}{} é {}{:.2f}{}.'.format(cores['ru'], n, cores['l'], cores['vdf'], pow(n, (1 / 2)),  # sqrt(n)
                                                       cores['l']))
