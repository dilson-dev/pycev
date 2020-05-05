# Exercício Python #065 - Maior e Menor valores

"""
DESAFIO 065
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se
ele quer ou não continuar a digitar valores.
"""

from time import sleep

res = 'S'
quantnum = somanum = maiornum = menornum = 0
while res in 'S':  # res == 'S'
    num = int(input('\nDigite um valor inteiro: '))
    quantnum += 1
    somanum += num
    if num > maiornum or quantnum == 1:
        maiornum = num
    if num < menornum or quantnum == 1:
        menornum = num
    '''
    if quantnum != 1:
        if num > maiornum:
            maiornum = num
        elif num < menornum:
            menornum = num
    else:
        maiornum = menornum = num
    '''
    res = ''
    while res not in 'SN' or res == '':
        res = input('\nQuer continuar a digitar valores? [S/N] ').upper().strip()[0]
        if res not in 'SN' or res == '':
            print('Erro, tente novamente.')

medianum = somanum / quantnum

print('\nAnalisando valores..'), sleep(3)

print(f'\nQuantidade de nºs digitada: {quantnum}.\nMédia: {medianum}.\nMaior nº: {maiornum}.\nMenor nº: {menornum}.')
#  {medianum:.1f}
