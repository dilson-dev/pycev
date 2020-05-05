# Curso Python #15 - Interrompendo repetições while

"""
n = s = 0
while True:   #  n != 999 com Gambiarra
    n = int(input('Digite um nº: '))
    if n == 999:
        break
    s += n
# s -= 999 Gambiarra
# print('\nA soma vale {}.'.format(s))
print(f'\nA soma vale {s}.')
"""

nome = 'José'
idade = 33
salario = 987.3

'''
print(f'O {nome} tem {idade} anos.')  # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # PYTHON 3
print('O %s tem %d anos.' % (nome, idade))  # %s tem %s/%i  # PYTHON 2 NÃO RECOMENDADO USAR NO PY 3
# Muitos cursos ainda ensinam da maneira antiga do PY 2.
'''

print(f'O {nome:–>20} tem {idade} anos e ganha R${salario:.2f}.')
# nome:20 coloca variável em 20 espaços
# nome:^20 centraliza variável em 20 espaços
# nome:–^20 centraliza e complementa os espaços vazios com o caracter –
# nome:–>20 Alinha à direita complementando espaços vazios com o caracter –
# nome:–<20 Alinha à esquerda '' ''


# Todas as formatações de string vistas antes funcionam c/ as F'strings usando o modo de interpolação.
