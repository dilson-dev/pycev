"""
DESAFIO 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares.
"""

nums = pares = ()  # nums = int(input('Digite um valor: ')), # pares = nums[0] if nums[0] % 2 == 0 else '',

for c in range(4):
    nums += int(input(f'Digite outro valor: ')),
    pares += nums[c] if nums[c] % 2 == 0 else '',

print(f'Você digitou os valores: {nums}.')
print(f'Vezes que o nº 9 foi digitado: {nums.count(9)}.')
if 3 in nums:
    print(f'Posição que foi digitado o primeiro valor 3: {nums.index(3) + 1}.')
else:
    print(f'O valor 3 não foi digitado, portanto não se encontra em nenhuma posição.')
print('Valores pares:', end=' ')

# print(pares[c] for c in range(len(pares)) if pares[c] % 2 == 0)

for c in range(4):
    if pares[c] != '':  # pares[c].isnumeric()
        print(pares[c], end=' ')
