"""
DESAFIO 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

total = 0

listagem = ()

'''
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Trasnferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
'''

while True:
    produto = input('\nNome do produto: ')
    if produto == '' or not produto.isalpha():
        break
    preco = input('Preço do produto: R$')
    if not preco.replace('.', '', 1).isnumeric() or float(preco) <= 0:
        break
    listagem += (produto, preco)  # (produto, preco),

print()
print('–' * 45)
print(f'|{" LISTAGEM DE PREÇOS ":^43}|')
print('–' * 45)
for i in range(0, len(listagem), 2):  # i in listagem:
    print(f'| {listagem[i]:.<32}R${float(listagem[i + 1]):>7.2f} |')  # i[0], i[1] total += listagem[i + 1]
total = sum(float(i) for i in listagem if i.replace('.', '', 1).isnumeric())
print('–' * 45)
print(f'| {"Total":.<32}R${total:>7.2f} |')
print('–' * 45)
