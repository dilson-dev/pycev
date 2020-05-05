# Exercício Python #088 - Palpites para a Mega Sena

"""
DESAFIO 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

palpites, nums = set(), set()  # [], []

print('', '–' * 35, f'|{"SORTEIO AUTOMÁTICO LOTERIA":^33}|', '–' * 35, sep='\n')

while True:
    qtdjogos = int(input('\nQuantos jogos quer sortear? (entre 1 e 10) '))
    if 1 <= qtdjogos <= 10:
        break

print('\n', '-=' * 3, f'  SORTEANDO {qtdjogos} JOGO(S)  ', '-=' * 3, '\n', sep='')

while len(palpites) < qtdjogos:  # j in range(qtdjogos)
    '''
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in nums:
            nums.append(num)
            cont += 1
    '''
    while len(nums) < 6:
        nums.add(randint(1, 60))
    palpites.add(tuple(sorted(nums)))  # palpites.append(sorted(nums))  # -> Ñ usa [:] pq o sorted já muda a estrutura
    nums.clear()
for num, jogo in enumerate(palpites, 1):
    sleep(1), print('Jogo', f'{num:2}:' if qtdjogos == 10 else f'{num}:', end=' ')
    [print(f'{n:>2}', end=' ') for n in jogo], print()  # sem sorted

print('\n', '-=' * 5, f' < BOA SORTE! > ', '-=' * 5, sep='')


# Com sample, sem firula, e com palpites alinhados e sleep, respectivamente:
'''
from random import sample as s
[print(j) for j in (sorted(s(range(1, 61), 6)) for n in range(int(input('\nPalpites: '))))]
'''
'''
from random import sample
from time import sleep
jogos = [sorted(sample(range(1, 61), 6)) for j in range(int(input('\nPalpites: ')))]
[(sleep(1), print(f'Jogo {n:>2} = [{", ".join(f"{v:>2}" for v in j)}].')) for n, j in enumerate(jogos, 1)]
'''
