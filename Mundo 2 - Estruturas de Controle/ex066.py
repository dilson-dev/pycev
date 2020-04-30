# Exercício Python #066 - Vários números com flag
"""
DESAFIO 066
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""

somanum = quantnum = 0

'''
num = soma = 0

"""
while num != 999:
    num = int(input('Digite um nº: '))
    soma += num
soma -= 999
"""
"""
while num != 999:
    soma += num
    num = int(input('Digite um nº: '))
"""

print(f'A soma dos números é {soma}.')
'''

while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    somanum += num
    quantnum += 1
num = int(input('\nDigite um número entre 0 e 20: '))
print(f'\nA soma dos {quantnum} valores digitados foi {somanum}.')
