# Exercício Python #030 - Par ou Ímpar?

"""
DESAFIO 030
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

from time import sleep
n = int(input('Digite um número: '))
print('Analisando...\n')
sleep(1.2)
if n % 2 == 0:
    print('Este número é par.')
else:
    print('Este número é ímpar.')

# Solução do vídeo:
'''
número = int(input('\033[35mMe diga um número qualquer: \033[m'))
resultado = número % 2
if resultado == 0:
    print('O número {} é \033[34mPAR\033[m.'.format(número))
else:
    print('O número {} é \033[34mÍMPAR\033[m.'.format(número))
'''
