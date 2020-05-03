# Exercício Python #019 - Sorteando um item na lista
from random import choice
n1 = str(input('\n\033[1;30mPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
a = [n1, n2, n3, n4]  # Alunos
r = choice(a)
print('O aluno sorteado foi \033[1;4;33m{}\033[1;30m.'.format(r))
