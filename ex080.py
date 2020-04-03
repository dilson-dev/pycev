"""
DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""
nums = [int(input('\nDigite um valor: '))]
print('Primeiro valor adicionado na lista, na posição 0.')

for c in range(1, 5):
    pos = 0
    num = int(input(f'\nDigite o {c + 1}º valor: '))
    for n in nums:
        if num > n:
            pos += 1
    nums.insert(pos, num)
    if nums[pos] == nums[-1]:
        print(f'Adicionado ao final da lista na posição {pos}.')
    elif pos == 0:
        print('Adicionado ao começo da lista na posição 0.')
    else:
        print(f'Adicionado na posição {pos} da lista.')
print()
print('=-' * 35)
print(f'Os valores digitados de forma ordenada foram: {nums}.')
print('=-' * 35)
