# Exercício Python #085 - Listas com pares e ímpares

"""
DESAFIO 085
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

nums = [[], []]
print()
for n in range(1, 8):  # 7/0, 7
    print('=-' * 16)
    num = int(input(f'Digite o {n}º valor: '))  # n + 1
    nums[num % 2].append(num)
    '''
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
    '''
print('=-' * 20)
print(f'Pares em ordem crescente: {sorted(nums[0])}.')
print(f'Ímpares em ordem crescente: {sorted(nums[1])}.')
print('=-' * 20)
