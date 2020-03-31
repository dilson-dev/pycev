"""
DESAFIO 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numsextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
               'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
               'dezessete', 'dezoito', 'dezenove', 'vinte')

res = 'S'

while res == 'S':
    while True:
        num = int(input('\nDigite um número entre 0 e 20: '))
        if num in range(21):  # 0 <= num <= 20:
            break
        print('Erro, tente novamente.', end='')
    print(f'\nO número {num} escrito por extenso é: {numsextenso[num].capitalize()}.')
    while True:
        res = input('\nQuer continuar? [S/N] ').upper()[0]
        if res in 'SN' and res != '':
            break

'''
numsextenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
               'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
'''

#  num = int(input('\nDigite um número entre 0 e 20: '))
# while num not in range(20):
# num = int(input('\nErro, tente novamente. Digite um número entre 0 e 20: '))

'''
while True:
    num = int(input('\nDigite um número entre 0 e 20: '))
    if num in range(20):
        break
'''
'''
for ind, elemento in enumerate(numsextenso):
    if num == ind:
        print(elemento)
'''
