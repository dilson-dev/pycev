# Exercício Python #084 - Lista composta e análise de dados

"""
DESAFIO 084
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves.
"""

pessoas, pesados, leves = [], [], []

print()

while True:
    print('=-' * 16)
    pessoas.append([input('Nome: '), float(input('Peso em KG: '))][::-1])
    print('=-' * 16)
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

"""
pessoas, dados, pesados, leves = [], [], [], []
pesomaior = pesomenor = c = 0

print()

while True:
    print('=-' * 16)
    dados.append(input('Nome: '))
    dados.append(float(input('Peso em KG: ')))
    if c == 0:
        pesomaior = pesomenor = dados[1]
    if dados[1] > pesomaior:
        pesomaior = dados[1]
    if dados[1] < pesomenor:
        pesomenor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print('=-' * 16)
    res = ''
    while not res or res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res == 'N':
        break
    c += 1

for pessoa in pessoas:
    if pessoa[1] == pesomaior:
        pesados.append(pessoa[1])
    if pessoa[1] == pesomenor:
        leves.append(pessoa[1])

print('=-' * 16, f'Quantidade de pessoas cadastradas: {len(pessoas)};', sep='\n')
print(f'Maior peso foi {pesomaior:.2f}KG. Peso de {pesados}.')
print(f'Menor peso foi de {pesomenor:.2f}KG. Peso de {leves}.')
"""

"""
pessoas, dados, pesados, leves = [], [], [], []
pesomaior = pesomenor = c = 0

print()

while True:
    print('=-' * 16)
    dados.append(input('Nome: '))
    dados.append(float(input('Peso em KG: ')))
    pessoas.append(dados[:])
    dados.clear()
    print('=-' * 16)
    res = ''
    while not res or res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res == 'N':
        break

for d in range(len(pessoas)):
    for j in [[pesomaior, pesados], [pesomenor, leves]]:
        if d == 0 or pessoas[d][1] > j[0]:
            j[1].clear()
            j[1].append(pessoas[d][0])
            j[0] = pessoas[d][1]
        elif pessoas[d][1] == j[0]:
            j[1].append(pessoas[d][0])

print('=-' * 16, f'Quantidade de pessoas cadastradas: {len(pessoas)};', sep='\n')
print(f'Maior peso foi {pesomaior:.2f}KG. Peso de {pesados}.')
print(f'Menor peso foi de {pesomenor:.2f}KG. Peso de {leves}.')
"""
