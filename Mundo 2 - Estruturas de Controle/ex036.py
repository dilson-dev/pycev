# Exercício Python #036 - Aprovando Empréstimo
vc = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
a = int(input('Anos de financiamento: '))
pm = vc / (a * 12)  # Parcelas mensais
n = s * 30/100
print('\nPara comprar uma casa de R${:.2f} em {} anos o valor das parcelas mensais será de R${:.2f}.'.format(vc, a, pm))
if pm > n:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
