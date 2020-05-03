# Exercício Python #078 - Maior e Menor valores na Lista
"""
DESAFIO 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

''' # Maneira mais enxuta:
n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
print(f'\nVocê digitou os valores {n}.')
print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')
'''

while True:
    quantnums = int(input('\nDigite a quantidade de números que deseja ler (de 1 a 10): '))
    if 0 < quantnums <= 10:
        break

nums = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(quantnums)]

print(), print('=-' * 40)

print(f'\nVocê digitou os valores {nums}.')
print(f'\nO maior nº digitado foi {max(nums)} nas posições '
      f'{", ".join([str(i) for i in range(len(nums)) if nums[i] == max(nums)])}.')
print(f'O menor nº digitado foi {min(nums)} nas posições '
      f'{", ".join([str(i) for i in range(len(nums)) if nums[i] == min(nums)])}.')

''' # Maneira mais extensa
listanum = []
posmai = []
posmen = []
mai = men = 0
for c in range(5):
    listanum.append(int(input(f'\nDigite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    elif listanum[c] > mai:
        mai = listanum[c]
    elif listanum[c] < men:
        men = listanum[c]
print('=-' * 30)
"""
print(f'\nPosições maior valor {mai}:', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')

print(f'\nPosições menor valor {men}:', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
"""

for i, v in enumerate(listanum):
    if v == mai:
        posmai += [i]
    if v == men:
        posmen += [i]

for ch in "[", "]":
    posmai = str(posmai).replace(ch, "")
    posmen = str(posmen).replace(ch, "")

print(f'\nPosições maior valor {mai}: {posmai}.')
print(f'Posições menor valor {men}: {posmen}.')
'''
n = [int(input(f'\nDigite um valor para a posição {pos}: ')) for pos in range(5)]
print(f'\nVocê digitou os valores {n}.')
print(f'\nMaior nº digitado foi {max(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == max(n))}.')
print(f'Menor nº digitado foi {min(n)} nas posições {", ".join(str(i) for i in range(5) if n[i] == min(n))}.')
