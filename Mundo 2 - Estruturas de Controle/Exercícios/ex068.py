# Exercício Python #068 - Jogo do Par ou Ímpar
"""
DESAFIO 068
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('–=' * 12)
print(f'|{"Jogo do par ou ímpar":^22}|')
print('–=' * 12)

vitorias = 0

while True:
    parOuImpar = ' '
    while parOuImpar not in 'PI' or parOuImpar == '':
        parOuImpar = input('\nPar ou ímpar? [P/I]: ').strip().upper()
        if parOuImpar != '':
            parOuImpar = parOuImpar[0]
    if parOuImpar == 'P':
        jogador = 0
    elif parOuImpar == 'I':
        jogador = 1
    while True:
        numeroJogador = int(input('\nQual valor quer jogar? '))
        if 0 <= numeroJogador <= 10:
            break
        print('\nErro. Você só pode jogar de 0 a 10.')
    numeroPc = randint(0, 10)
    somaNumeros = numeroJogador + numeroPc
    print('–' * 34)
    print(f'Você jogou {numeroJogador} e o computador {numeroPc}.')
    print(f'{numeroJogador} + {numeroPc} é {somaNumeros} e', 'deu PAR' if somaNumeros % 2 == 0 else 'deu ÍMPAR')
    print('–' * 34)
    if somaNumeros % 2 != jogador:
        print('Você PERDEU')
        print('–=' * 17)
        break
    print('Você VENCEU!')
    print('Vamos jogador novamente...')
    print('–=' * 17)
    vitorias += 1

print(f'GAME OVER! Você teve {vitorias} vitória(s).')

'''
"""
Maneira mais enxuta mostrada no vídeo, mudei as condições diminuindo em 8 linhas o código, porém este não valida o
valor dado pelo usuário, portanto se digitar negativo, ou qualquer outro valor que não esteja entre 0 e 10 o programa
continua
"""
from random import randint
v = 0
while True:
    jogador = int(input('\nDigite o valor que quer jogar: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {total}.', end=' ')
    print('DEU', 'PAR' if total % 2 == 0 else 'ÍMPAR')
    if (tipo == 'P' and total % 2 == 0) or (tipo == 'I' and total % 2 == 1):
        print('Você venceu.')
        v += 1
    else:
        print('Você perdeu.')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
'''
