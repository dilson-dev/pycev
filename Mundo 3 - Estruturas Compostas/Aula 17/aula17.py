# Curso Python #17 - Listas (Parte 1)

a = [2, 3, 4, 7]
b = a[:]  # b = a

b[2] = 8

print(f'Lista A: {a}.')
print(f'Lista B: {b}.')

'''
valores = list()  # []

for cont in range(5):
    valores.append(int(input('Digite um valor: ')))
'''

'''
valores.append(5)
valores.append(9)
valores.append(4)
'''
'''
print(' - '.join(str(valor) for valor in valores))
print('...'.join([f'{pos + 1}º {valor}' for pos, valor in enumerate(valores)]))

vp = [f'{pos + 1}º = {valor}' for pos, valor in enumerate(valores)]
print(', '.join(vp))
'''

'''for valor in valores:
    print(valor, end=' ')'''

'''
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
'''

'''
nums = [2, 5, 9, 1]
nums[2] = 3
nums.append(7)  # nums[4] = 7 PHP faz dessa forma, mas dá erro no Python.
nums.sort(reverse=True)
nums.insert(2, 2)
if 5 in nums:
    nums.remove(5)
else:
    print('Não achei o número 5.')
"""while 2 in nums:
    nums.remove(2)"""
# nums.pop(2)
print(nums)
print(f'Essa lista tem {len(nums)} elementos.')
'''
