# Exercício Python #010 - Conversor de Moedas

"""
DESAFIO 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considere US$1,00 = R$3,27
"""

print('\033[1;36mConversor de reais para moedas estrangeiras e criptomoeda bitcoin.')
r = float(
    input('\033[32mQuantos dinheiro em reais você tem na carteira? R$'))  # Real
dol = r / 4.02  # Dólar
eur = r / 4.51  # Euro(€)
lb_est = r / 5.11  # Libra esterlina(£), moeda oficial do Reino Unido.
ien = r * 27.17  # Iene
bc = r / 32448.46  # Bitcoin
print(
    '\033[1;30m\nConforme cotação de 25 de maio de 2019 com \033[1;32mR${:.2f}\033[1;30m você pode comprar:'.format(r))
print('\033[1;35;m\nUS${:.2f}\n€{:.2f}\n£{:.2f}\n¥{:.2f}\n₿{:.6f}\033[m'.format(
    dol, eur, lb_est, ien, bc))

"""
Eu observei o dia no Python Console enquanto ele fazia operações para demonstrar como funciona os operadores aritméticos
Aí peguei e coloquei no print para dar ênfase que essa cotação não é de hoje em dia. Não tinha notado, mas se for de
fato essa data ele demorou uns 2 meses e meio +- para postar o vídeo partindo do momento que ele gravou para a postagem
do vídeo.
"""
