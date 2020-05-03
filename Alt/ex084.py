pessoas, pesados, leves = [], [], []
while True:
    pessoas.append([input('\nNome: '), float(input('Peso em KG: '))][::-1])
    res = ''
    while not res or res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res == 'N':
        break
for dado in pessoas:
    if dado[0] == max(pessoas)[0]:
        pesados.append(dado[1])
    if dado[0] == min(pessoas)[0]:
        leves.append(dado[1])
print('=-' * 16, f'Quantidade de pessoas cadastradas: {len(pessoas)};', sep='\n')
print(f'Maior peso foi {max(pessoas)[0]:.2f}KG. Peso de {pesados}')
print(f'Menor peso foi de {min(pessoas)[0]:.2f}KG. Peso de {leves}.')

'''
cadastros = []
mai = men = 0
while True:
    cadastros.append([input('\nNome: '), float(input('Peso: '))][::-1])
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break
print(f'\nCadastro(s): {len(cadastros)}.')
for m in [['Maior', max(cadastros)[0]], ['Menor', min(cadastros)[0]]]:
    print(f'\n{m[0]} peso: {m[1]}Kg. Peso de', end=' ')
    for dado in cadastros:
        if dado[0] == m[1]:
            print(f'[{dado[1]}]', end=' ')
print()
'''
