"""
DESAFIO 082
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.

Ao final, mostre o conteúdo doas três listas geradas.
"""
nums = list()
numspares = []
numsimpares = []

while True:
    num = int(input('\nDigite um valor: '))
    nums.append(num)  # nums.append(int(input('\nDigite um valor: '))
    '''
    if num % 2 == 0:
        numspares.append(num)
    else:
        numsimpares.append(num)
    '''
    res = ' '
    while res not in 'SN' and res != '':
        res = input('Quer continuar? [S/N] ').strip().upper()[0]
    if res == 'N':
        break

for num in nums:
    if num % 2 == 0:
        numspares += [num]
    else:
        numsimpares += [num]

print()
print('=-' * 35)
print(f'Lista dos valores: {nums}.\nLista dos pares: {numspares}.\nLista dos ímpares: {numsimpares}.')
print('=-' * 35)
