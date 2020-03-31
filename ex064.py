"""
DESAFIO 064
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""

numeros = numsoma = 0

''' Gambiarra
num = 0
while num != 999:
    num = int(input('\nDigite um número inteiro [999 para parar]: '))
    if num != 999:
        numeros += 1
        numsoma += n

# num -= 999 Gambiarra pesada
'''

n = int(input('\nDigite um número interio [999 para parar]: '))
while n != 999:
    numsoma += n
    numeros += 1
    n = int(input('\nDigite um número inteiro [999 para parar]: '))

print(f'\nQuantidade de números digitada: {numeros}.\nSoma dos números digitados: {numsoma}.')

'''
nums = [0]

while nums[-1] != 999:
    nums += [int(input('\nDigite um número inteiro [999 para parar]: '))]
print(f'\nForam digitados {len(nums) - 2} números e a soma entre eles é {sum(nums) - 999}.')
'''
