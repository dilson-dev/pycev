# Exercício Python #015 - Aluguel de Carros

"""
DESAFIO 015
Escreva um programa que pergunte a quantidade Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('\033[33mAlugacar\033[1;30m, alugue um carro e dê um rolê pelo asfalto!\033[m')
dias = int(input('\nPor quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodado(s)? '))
total = (dias * 60) + (km * 0.15)
print('\nO total a pagar é de \033[1;32mR${:.2f}\033[m.'.format(total))
