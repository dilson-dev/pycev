# Exercício Python #044 - Gerenciador de Pagamentos
vp = float(input('Qual o valor total das compras? R$'))
print('''\nFormas de pagamento\n
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
fp = int(input('\nDigite a forma de pagamento: '))
if fp == 1:
    print('\nO produto custará R${:.2f}.'.format(vp * 0.9))
elif fp == 2:
    print(f'O produto custará R${vp * 0.95:.2f}.')
elif fp == 3:
    print('O produto custará R${:.2f} em 2 parcelas de R${:.2f}.'.format(vp, vp/2))
elif fp == 4:
    p = int(input('Quantas parcelas? '))
    print('\nO produto custará R${:.2f} em {} parcelas de R${:.2f}. '.format(vp * 1.2, p, vp * 1.2/p))
else:
    print('\033[1;31m\nOpção inválida. Tente novamente!')

"""
print('\n' + f'{" LOJA ":=^40}')
pc = float(input('\nPreço das compras: R$'))
print('''\n\n\033[1;33mFORMAS DE PAGAMENTO\033[m\n
[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
fp = int(input('\nDigite a opção desejada: '))  # Forma de pagamento
if fp == 1:
    t = pc - (pc * 10 / 100)
elif fp == 2:
    t = pc - (pc * 5 / 100)
elif fp == 3:
    t = pc
    print(f'\nSua compra será parcelada em 2x de R${t/2:.2f} sem juros.')
elif fp == 4:
    t = pc + (pc * 20/100)
    p = int(input('Quantas parcelas? '))
    print(f'\nSua compra será parcelada em {p}x de R${t/p:.2f} com juros.')
else:
    t = pc
    print('\n\033[1;31mOpção de pagamento inválida.\033[m Tente novamente.')
print(f'\nSua compra de R${pc:.2f} vai custar R${t:.2f} no final.')
"""
