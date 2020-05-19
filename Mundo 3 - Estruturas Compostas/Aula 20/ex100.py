# Exercício Python #100 - Funções para sortear e somar

"""
DESAFIO 100
Faça um programa que tenha uma lista chamada números e duas funções chamdas sorteia() e somaPar(). A
primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    sleep(1)
    for cont in range(5):
        # 1ª maneira:
        '''
        sorteado = randint(1, 10)
        print(sorteado, end=' ', flush=True)
        sleep(0.3)
        lista.append(sorteado)
        '''

        # 2ª maneira:
        lista.append(randint(1, 10))
        print(lista[cont], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def soma_par(lista):

    # 1ª Solução:
    '''
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    '''

    # 2ª Solução
    soma = sum([num for num in lista if num % 2 == 0])

    print(f'Somando os valores pares de {lista}, temos {soma}.')


# Programa Principal
números = list()
sorteia(números)
soma_par(números)
