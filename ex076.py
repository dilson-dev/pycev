"""
DESAFIO 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

produtos = ()

total = 0

while True:
    produtos += input('\nNome do produto: '),
    if produtos[-1] == '':
        break
    produtos += float(input('Preço do produto: R$')),
    if produtos[-1] == 0.0:
        break

print()
print('–' * 45)
print('|{:^43}|'.format(' LISTAGEM DE PREÇOS '))
print('–' * 45)
for c in range(0, len(produtos) - 2, 2):
    print(f'| {produtos[c]:.<32}R${produtos[c + 1]:>7.2f} |')  # {produtos[c + 1]:^5.2f} |')
    total += produtos[c + 1]
print('–' * 45)
print(f'| {"Total":.<32}R${total:>7.2f} |')
print('–' * 45)
