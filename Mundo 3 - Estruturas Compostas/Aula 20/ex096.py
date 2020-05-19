# Exercício Python #096 - Função que calcula área

"""
DESAFIO 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def área(largura, comprimento):
    # 1ª Solução:
    '''
    a = largura * comprimento  # Cálculo da área retangular
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')
    '''

    # 2ª Solução:
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento}m².')


'''
def titulo(msg):
    print(f'\n {msg} ')
    print('-' * len(msg))
'''

# Programa principal
# titulo('Controle de Terrenos')

print('\nControle de Terrenos')
print('-' * 20)

# 1ª Solução:
'''
larg = float(input('Largura em metros: '))
comp = float(input('Comprimento em metros: '))

área(larg, comp)
'''

# 2ª Solução:
área(largura=float(input('Largura em metros: ')), comprimento=float(input('Comprimento em metros: ')))
