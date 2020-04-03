"""
DESAFIO 081
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
nums = []
while True:
    '''
    num = int(input('\nDigite um número'))
    nums.append(num)
    '''
    nums += [int(input('\nDigite um número: '))]
    while True:
        res = input('Quer continuar? [S/N] ').strip().upper()[0]
        if res in 'SN' and res != '':
            break
    if res == 'N':
        break
print()
print('=-' * 40)
print(f'Foram digitados {len(nums)} elementos.')

nums.sort(reverse=True)

print(f'Os valores em ordem descrescente são: {nums}.')

if 5 in nums:
    posicoes = ' '.join([str(num) for num in range(len(nums)) if nums[num] == 5])
    print(f'O valor 5 faz parte da lista, e aparece {nums.count(5)} vez(es) na(s) posição(ões) {posicoes}.')
else:
    print('O valor 5 não foi encontrado na lista.')
print('=-' * 40)
