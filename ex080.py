"""
DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

nums = list()
for c in range(5):
    pos = 0
    num = int(input(f'\nDigite o {c + 1}º valor: '))

    for elemento in nums:
        if num > elemento:
            pos += 1
        else:
            break

    ''' # Outra maneira de definir a posição do número, porém mais complicada de entender:
    while c != 0 and pos < len(nums) and num > nums[pos]:  # nums != [] and ... and ...
        pos += 1
    '''

    nums.insert(pos, num)
    if c == 0:
        print('Adicionado à lista na posição 0.')
    else:
        if nums[pos] == nums[-1]:  # nums[len(nums) - 1]
            parte = 'final'
        elif pos == 0:
            parte = 'começo'
        else:
            parte = 'meio'
        print(f'Adicionado na posição {pos} no {parte} da lista.')
print(), print('=-' * 35)
print(f'Os valores digitados de forma ordenada foram: {nums}.')
print('=-' * 35)

''' # Solução do Professor Guanabara com uma técnica "diferente", diria até o inverso do que fiz na parte da posição.
nums = []
for c in range(5):
    num = int(input(f'\nDigite o {c + 1}º valor: '))
    if c == 0 or num > nums[-1]:
        nums.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(nums):
            if num <= nums[pos]:
                nums.insert(pos, num)
                print(f'Valor adicionada na posição {pos}...')
                break
            pos += 1
print()
print('=-' * 33)
print(f'Valores digitados na forma ordenada: {nums}')
print('=-' * 33)
'''
