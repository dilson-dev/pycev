"""
DESAFIO 070
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total de gasto na compra;
B) Quantos produtos custam mais de R$1000;
C) Qual é o nome do produto mais barato.
"""

total = totmil = menor = cont = 0

barato = ''

print()
print('–' * 30)
print(f'|{"LOJA 1,99":^28}|')  # print('|{:^28}|'.format('LOJA 1,99'))

while True:
    print('–' * 30)
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if preco < menor or cont == 1:
        menor = preco
        barato = produto

    print('–' * 30)
    '''while True:
        res = input('Quer continuar? [S/N] ').strip().upper()[0]
        if res in 'SN' and res != '':
            break
        print('Erro, tente novamente.')'''
    res = ' '
    while res not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()[0]
        if res not in 'SN':
            print('Erro, tente novamente.')
    if res == 'N':
        break


print()
print(f'{" FIM DO PROGRAMA ":–^40}')
print(f'\nGasto total: R${total:.2f};\nProdutos acima de R$1000.00: {totmil};'
      f'\nProduto mais barato: {barato} (R${menor:.2f}).')
