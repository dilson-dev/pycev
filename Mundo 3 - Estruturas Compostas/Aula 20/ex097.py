# Exercício Python #097 - Um print especial

"""
DESAFIO 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adptável.

Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""


def escreva(frase):
    # 1ª Solução:
    '''
    tam = len(frase) + 2

    print('~' * tam)
    print(f' {frase}')
    print('~' * tam)
    '''

    # 2ª Solução:
    print(f'{(len(frase) + 4) * "~"}\n| {frase} |\n{(len(frase) + 4) * "~"}')


# Programa Principal

# Inserindo parâmetros manualmente:
'''
escreva('Olá, Mundo!')
escreva('Delfino')
escreva('Curso de Python no YouTube')
escreva('CeV')
'''

# Com input:
# escreva(input('\nFrase: '))

# Com input e repetição:
while True:
    i = input('\nFrase (vazio para parar): ')
    if i == '':
        break
    escreva(i)
