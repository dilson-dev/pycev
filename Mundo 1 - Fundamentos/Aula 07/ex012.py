# Exercício Python #012 - Calculando Descontos

"""
DESAFIO 012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


Regra de 3:

R$10    100 %
    \\//
    //\\
   x    5%

10*5/100 = 0.5  (5 por cento de 10)
1500*10/100 = 150.0 (10 por cento de 1500)
875*15/100 = 131.25 (15 por cento de 875)
"""

p = float(input('\033[32mQual o preço do produto? R$\033[m'))
# n = p - (p * 5 / 100)
print('O produto com o custo de \033[1;32mR${:.2f}\033[m, está'.format(p), end=' ')
print('com \033[1;35m5%\033[m de desconto na promoção. Seu custo será de \033[1;36mR${:.2f}\033[m.'.format(p * 0.95))
