# Exercício Python #016 - Quebrando um número

"""
DESAFIO 016
Crie um programa que leia um número Real (float) qualquer pelo teclado e mostre na tela a sua porção Inteira.

Ex:
Input - Digite um número: 6.127
Output - O número 6.127 tem a parte Inteira 6.
"""

num = float(input('\033[1;30mDigite um número qualquer: \033[m'))
print('A porção inteira de {}{}{} é {}{}{}.'.format('\033[32m', num, '\033[m', '\033[1;35m', int(num), '\033[m'))
