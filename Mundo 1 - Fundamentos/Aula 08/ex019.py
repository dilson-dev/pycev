# Exercício Python #019 - Sorteando um item na lista

"""
DESAFIO 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome do escolhido.
"""

from random import choice
n1 = str(input('\n\033[1;30mPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
a = [n1, n2, n3, n4]  # Alunos
r = choice(a)
print('O aluno sorteado foi \033[1;4;33m{}\033[1;30m.'.format(r))
