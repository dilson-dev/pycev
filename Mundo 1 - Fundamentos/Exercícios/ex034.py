# Exercício Python #034 - Aumentos múltiplos
s = float(input('\033[1;30mDigite o salário do funcionário: R$'))
print()
if s > 1250:
    t = 10
    a = s * 1.1
else:
    t = 15
    a = s * 1.15
print('\033[1;33mO salário do funcionário que era R${:.2f} vai aumentar em {}% para R${:.2f}.'.format(
    s, t, a))


s = float(input('\033[1;30mQual é o salário do funcionáraio? R$\033[m'))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print(
    'Quem ganhava \033[1;34mR${:.2f}\033[m passa a ganhar \033[1;35mR${:.2f}\033[m agora.'.format(s, n))

# Parênteses inúteis na variável n, pois a ordem de precedência já faz o cálculo na ordem.
