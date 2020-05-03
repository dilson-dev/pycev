# Exercício Python #081 - Extraindo dados de uma Lista
"""
DESAFIO 081
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
nums = list()
while True:
    nums.append(int(input('\nDigite um número')))
    res = ''
    while res == '' or res[0] not in 'SsNn':
        res = input('Quer continuar? [S/N] ').strip()
    if res[0] in 'Nn':
        break
print(), print('=-' * 40)
print(f'Foram digitados {len(nums)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(nums, reverse=True)}.')
if 5 in nums:
    print('O valor 5 faz parte da lista.')
    posicoes = ' '.join([str(num + 1) for num in range(len(nums)) if nums[num] == 5])
    palavpos = 'vez na posição' if len(posicoes) == 1 else 'vezes nas posições'
    print(f'Digitado {nums.count(5)} {palavpos} {posicoes},', end=' ')
    nums.sort(reverse=True)
    posicoes = ' '.join([str(num) for num in range(len(nums)) if nums[num] == 5])
    palavpos = 'na posição' if len(posicoes) == 1 else 'nas posições'
    print(f'aparecendo {palavpos} {posicoes} na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
print('=-' * 40)
