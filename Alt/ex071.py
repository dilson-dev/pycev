print()
print('=' * 40)
print('|{:^38}|'.format('Caixa Eletrônico'))
print('=' * 40)
valor = int(input('Quanto deseja sacar? R$'))
print('=' * 40)
for cedula in [50, 20, 10, 1]:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade != 0:
        print(f'{quantidade} cédulas de R${cedula:.2f}')
print('=' * 40)
'''
saque = int(input('\nValor do saque: R$'))
print('=' * 40)
for cedula in [50, 20, 10, 1]:
    quantidade = saque // cedula
    saque %= cedula
    if quantidade > 0:
        print(f'{quantidade} notas de R${cedula:2}')
'''
