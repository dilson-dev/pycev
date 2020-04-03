"""
DESAFIO 079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
"""
nums = list()  # []
while True:
    n = int(input('\nDigite um valor: '))
    if n not in nums:
        nums.append(n)  # nums += [n]
        print('Valor adicionado com sucesso...')
    else:
        print('Valores duplicados não são adicionados, tente digitar outro.')
    while True:
        res = input('\nQuer continuar? [S/N] ').strip().upper()[0]
        if res not in 'SN' and res != '':
            print('Erro, tente novamente.')
        else:
            break
    if res == 'N':
        break

nums.sort()

print()
print('=-' * 35)
print(f'Números digitados em ordem crescente: {str(nums).replace("[", "").replace("]", "")}.')
print('=-' * 35)
