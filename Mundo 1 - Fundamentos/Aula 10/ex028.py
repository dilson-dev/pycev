# Exercício Python #028 - Jogo da Adivinhação v.1.0

"""
DESAFIO 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""

from random import randint

n = int(input('Tente adivinhar o número escolhido pelo computador de 0 a 5: '))
pc = randint(0, 5)  # Faz o computador "escolher"
if n == pc:
    print('\nParabéns você acertou o número e venceu!')
else:
    print('\nQue pena você errou, na próxima quem sabe?')
    print('\nO número escolhido foi: {}.'.format(n))
    print('O número sorteado foi: {}.'.format(pc))


'''
from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador "PENSAR".

cores = {'limpar': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m'}

print(('{}-=-'.format(cores['amarelo'])) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...'.format(cores['azul']))
print('{}-=-{}'.format(cores['amarelo'], cores['limpar']) * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar.
print('{}PROCESSANDO...'.format(cores['roxo']))
sleep(3)
if jogador == computador:
    print('{}PARABÉNS! Você conseguiu me vencer!'.format(cores['verde']))
else:
    print('{}GANHEI! Eu pensei no número {} e não no {}!'.format(cores['vermelho'], computador, jogador))
'''
