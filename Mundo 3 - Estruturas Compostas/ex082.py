# Exercício Python #082 - Dividindo valores em várias listas
"""
DESAFIO 082
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.

Ao final, mostre o conteúdo doas três listas geradas.
"""
nums = []
pares = []
impares = []

while True:
    nums += [int(input('\nDigite um valor: '))]
    if nums[-1] % 2 == 0:
        pares += [nums[-1]]
    else:
        impares += [nums[-1]]
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break

listas = []
for lista in [nums, pares, impares]:
    listas += [str(lista).replace('[', '').replace(']', '')]

print(), print('=-' * 35)
print(f'Lista dos valores: {nums}.')
print(f'Lista dos pares: {pares}.' if pares else 'Nenhum número par foi digitado.')
print(f'Lista dos ímpares: {impares}.' if impares else 'Nenhum número ímpar foi digitado.')

'''
li = [pares, 'par', impares, 'ímpar']
print(' '.join(f'Lista dos {li[c + 1] + "es"}: {li[c]}.' if li[c] else f'Nenhum nº {li[c + 1]} foi digitado.' for c in
range(0, len(li), 2)))

for c in range(0, len(li), 2):
    print(f'Lista dos {li[c + 1] + "es"}: {li[c]}.' if li[c] else f'Nenhum nº {li[c + 1]} foi digitado.')
'''

print('=-' * 35)
