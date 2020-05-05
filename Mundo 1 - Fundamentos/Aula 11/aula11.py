# Curso Python #11 - Cores no Terminal


# print('\033[7;33;46mOlá, Mundo!\033[m')
"""
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
"""

nome = 'Delfino'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá muitp prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
# print('Olá muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

'''
Pode-se usar cores ANSI escape sequence de três formas:
dentro da própria string (mais legível, e simples)
com .format na {} (menos legível, e mais complicado)
dicionários + .format na {}. (com f' (F string) até que é interessante a ideia)

OBS: Não confundir ANSI com ASCII.
'''
