# Exercício Python #035 - Analisando Triângulo v1.0
r1 = float(input('\n\033[1;33mDigite o comprimento da reta 1: '))
r2 = float(input('\033[1;34mDigite o comprimento da reta 2: '))
r3 = float(input('\033[1;35mDigite o comprimento da reta 3: '))

if r1 + r2 <= r3 or r2 + r3 <= r1 or r3 + r1 <= r2:
    p = ' não '
else:
    p = ' '
print('\n\033[1;30mOs comprimentos acima{}podem formar um triângulo.'.format(p))

"""
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
"""
