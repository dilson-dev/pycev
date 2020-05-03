nums = [[], []]
for n in range(1, 8):
    num = int(input(f'\nDigite o {n}º valor: '))
    nums[num % 2].append(num)
print('=-' * 20, f'Pares em ordem crescente: {sorted(nums[0])}.', sep='\n')
print(f'Ímpares em ordem crescente: {sorted(nums[1])}.')
