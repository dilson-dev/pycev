"""
DESAFIO 071
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print()

print('=' * 35)
print(f'|{"BANCO DO BRASIL":^33}|')
print('=' * 35)
valor = int(input('Qual valor deseja sacar? R$'))
print('=' * 35)

cedulas = [50, 20, 10, 1]

c = 0

while True:
    if valor >= cedulas[c]:
        cedula = cedulas[c]
        totcedulas = valor // cedula
        print(f'Total de {totcedulas:2} cédula(s) de R${cedula:.2f}')
        valor %= cedula
    if valor == 0:
        break
    c += 1

print('=' * 35)
print('Volte sempre ao BANCO DO BRASIL!\nTenha um bom dia!')
print('=' * 35)
