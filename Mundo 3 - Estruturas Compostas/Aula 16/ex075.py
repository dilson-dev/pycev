# Exercício Python #075 - Análise de dados em uma Tupla

"""
DESAFIO 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares.
"""

# nums = ()

'''
nums = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o último valor: ')))
'''

nums = tuple(int(input(f'Digite o {i+1}º numero: ')) for i in range(4))

'''
for c in range(1, 5):
    nums += int(input(f'\nDigite o {c}º valor: ')),
'''

print(f'\nVocê digitou os valores: {nums}.')
print(f'\nVezes que o nº 9 foi digitado: {nums.count(9)}.')
if 3 in nums:
    print(f'Posição que foi digitado o primeiro valor 3: {nums.index(3) + 1}ª.')
else:
    print('O valor 3 não foi digitado, portanto não se encontra em nenhuma posição.')

print('Valores pares:', ' '.join(str(num) for num in nums if num % 2 == 0))

'''
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')
'''

print()
