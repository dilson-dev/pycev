# Exercício Python #032 - Ano Bissexto

"""
DESAFIO 032
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

from datetime import date
ano = int(input('\033[1;30mDigite um ano para ver se ele é bissexto, para ver o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year  # Mostra o ano atual
if str(ano / 4)[-1] == '0' and str(ano / 100)[-1] != '0' or str(ano / 400)[-1] == '0':
    print('{}{} é um ano bissexto.'.format('\033[1;32m', ano))
else:
    print('{}{} não é um ano bissexto.'.format('\033[1;31m', ano))

# Solução do vídeo:
'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
'''
