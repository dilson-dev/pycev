# Exercício Python #048 - Soma ímpares múltiplos de três

"""
DESAFIO 048
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 até 500.
"""

s = 0
for c in range(3, 500, 6):  # Como os múltiplos de ímpares se alternam entre par e ímpar, o 6 pula os m. pares.
    s += c
print(s)


# Maneira mais resumida e enxuta, em apenas uma linha:
# print(sum(range(3, 500, 6)), sep='')

# A função range cria uma lista conforme os argumentos passados, onde 3 é o valor inicial, 500 o último valor,
# que não entra na lista, indo até 499, e 6 o passo.

# E, por fim, a função 'sum' do inglês 'soma', pega todos os valores dessa lista e retorna sua soma.


'''
repeticoes = 0
soma = 0
valores = 0

for c in range(1, 500, 2):  # era range(1, 501, 2), mas como 500 é par seria descartado de qualquer maneira.
    repeticoes += 1
    if c % 3 == 0:
        soma += c
        valores += 1

print(repeticoes, valores, soma)
'''


# Soma números ímpares múltiplos de outro número ímpar no intervalo desejado:

'''
multiplo = 0
while multiplo % 2 == 0:
    multiplo = int(input('\nMúltiplo ímpar: '))
intervalo = int(input('\nIntervalo: '))
for c in range(multiplo, intervalo + 1, multiplo * 2):
    s += c
    v += 1
print('\nA soma de todos os\033[1;34m', v, '\033[mvalores solicitados é:\033[1;32m', str(s) + '\033[m.')
'''

'''
num = 0
while num % 2 == 0:
    num = int(input('\nNúmero ímpar: '))

intervalo = int(input('\nIntervalo: '))

nums = [i for i in range(num, intervalo + 1, num * 2)]

print('\nA soma de todos os\033[1;34m', len(nums), '\033[mvalores solicitados é\033[1;32m', str(sum(nums)) + '\033[m.')
'''
