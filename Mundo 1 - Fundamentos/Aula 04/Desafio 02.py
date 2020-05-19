# Desafio 02

"""
Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data
formatada.
"""

print('=' * 5, ' DESAFIO 02 ', '=' * 5)

print('Qual sua data de nascimento?')

dia = input('Dia? ')
mes = input('Mês? ')
ano = input('Ano? ')

print()
print('Você nasceu no dia', dia, 'de', mes, 'de', ano)

print()
confirma = input('Certo? ')


# Outra solução conforme exigência da aula 11 onde é pedido para colocar cores em todos os exercícios anteriores:
"""
from time import sleep

cores = {'branco': '\033[30m',
         'azul': '\033[34m',
         'azul fraco': '\033[36m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'roxo': '\033[35m',
         'limpar': '\033[m'}

print('{}Qual sua data de nascimento? '.format(cores['branco']))
dia = input('{}Dia? '.format(cores['azul']))
mes = input('{}Mês? '.format(cores['amarelo']))
ano = input('{}Ano? '.format(cores['vermelho']))
print('{}Você nasceu no dia{}'.format(cores['limpar'], cores['roxo']), dia, 'de', mes, 'de', ano,)
print('{}Espero que esteja certo, pois coloquei conforme o que você inseriu. '.format(cores['verde']))
sleep(1.5)
print('{}Agradeço por sua paciência.'.format(cores['azul fraco']))
"""
