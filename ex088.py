"""
DESAFIO 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

palpites = []
numeros = []

print(), print('–' * 35)  # print('\n', '–' * 35, sep='')
print(f'|{"SORTEIO AUTOMÁTICO MEGA SENA":^33}|')
print('–' * 35)
while True:
    qtdjogos = int(input('\nQuantos jogos quer sortear? (entre 1 e 10) '))
    if 1 <= qtdjogos <= 10:
        break

print('\n', '-=' * 3, f'  SORTEANDO {qtdjogos} JOGO(S)  ', '-=' * 3, '\n', sep='')

for j in range(qtdjogos):
    for s in range(6):
        while True:
            numero = randint(1, 60)
            if numero not in numeros:
                break
        numeros.append(numero)
    palpites.append(numeros[:])
    numeros.clear()

for num, jogo in enumerate(palpites, 1):
    # jogo.sort()
    sleep(1.2)
    print('Jogo', f'{num:2}:' if qtdjogos == 10 else f'{num}:', sorted(jogo))
print('\n', '-=' * 5, f' < BOA SORTE! > ', '-=' * 5, sep='')
