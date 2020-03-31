r1 = float(input('\nDigite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
print('\nOs segmentos acima', end=' ')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:  # elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Isósceles.')
else:
    print('não podem formar um triângulo.')

'''
São chamadas condições aninhadas, uma dentro da outra, conforme se faz aninhamentos.
'''