# Curso Python #10 - Condições (Parte 1)

"""
nome = str(input('Qual é seu nome? '))
if nome == 'Delfino':  # Estrutura condicional simples só com if.
    print('Que nome lindo você tem!')
else:  # Estrutura condicional composta quando tem else.
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:  '))
m = (n1 + n2) / 2
print('Sua média é {:.1f}.'.format(m))
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')  # Condição simplificada (apenas 1 linha, comparada a 4).

''' 

Estrutura normal/comum, não simplificada:

if m >= 6.0:
    print('\nVocê está acima da média, parabéns!'.format(m))
else:
    print('\nSua média está baixa. Estude mais!')

'''
