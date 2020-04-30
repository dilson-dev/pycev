# Exercício Python #060 - Cálculo do Fatorial
"""
DESAFIO 060
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
"""

# from math import factorial

n = numero = int(input('Digite o número que deseja ver o fatorial: '))

# print(factorial(numero))

negativo = ''

if numero < 0:
    numero -= (numero * 2)
    negativo = '(-) '
    print(negativo, end='')

fatorial = 1
print(f'{numero}!', end=' = ')  # end='! = '
# print(*range(numero, 0, -1), sep=' x ', end=' = ')
while numero > 0:
    print(numero, 'x ' if numero > 1 else '= ', end='')
    fatorial *= numero
    numero -= 1

'''
for numf in range(numero, 0, -1):
    if numf != 1:
         print(f'{numf}', end='x')
    else:  # numf == 1
        print(f'{numf}', end=' = ')
    fatorial *= numf
'''

if negativo != '':
    print(negativo, end='')

print(fatorial)
