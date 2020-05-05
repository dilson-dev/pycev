# Exercício Python #034 - Aumentos múltiplos

"""
DESAFIO 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('\033[1;30mDigite o salário do funcionário: R$'))
print()
if s > 1250:
    t = 10
    a = s * 1.1  # s + (s * t / 100)
else:
    t = 15
    a = s * 1.15  # s + (s * t / 100)
print('\033[1;33mO salário do funcionário que era R${:.2f} vai aumentar em {}% para R${:.2f}.'.format(s, t, a))

# Mais resumido (sem a variável t):
'''
s = float(input('\033[1;30mQual é o salário do funcionáraio? R$\033[m'))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print('Quem ganhava \033[1;34mR${:.2f}\033[m passa a ganhar \033[1;35mR${:.2f}\033[m agora.'.format(s, n))
'''

# Parênteses inúteis na variável n, pois a ordem de precedência já faz o cálculo na ordem.
