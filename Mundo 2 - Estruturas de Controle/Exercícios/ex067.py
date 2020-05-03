# Exercício Python #067 - Tabuada v3.0
"""
DESAFIO 067
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    num = int(input('\nDigite um valor para ver sua tabuada: '))
    print('–' * 20)
    if num < 0:
        break
    for c in range(11):
        print(f'{num} x {c:2} = {num * c}')
    print('–' * 20)
print('Programa Tabuada encerrado. Volte sempre!')
