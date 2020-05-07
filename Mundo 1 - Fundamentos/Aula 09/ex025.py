# Exercício Python #025 - Procurando uma string dentro de outra

"""
DESAFIO 025
Crie um prograam que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""


"""
nome = str(input('Digite o seu nome completo: '))
silva = 'Silva' in nome
print('Tem "Silva" em seu nome? {}.'.format(silva))
"""

nome = str(input('\033[1;30mqual é o seu nome completo? ')).strip()
print('\033[1;34mSeu nome tem \'Silva\'? {}.'.format('silva' in nome.lower().split()))

"""
O operador in retorna um valor booleano indicando se o valor a esquerda existe no valor a direita deste.
E o método split retorna uma lista que divide os caracteres conforme os espaços dados, assim, é divido
entre palavras, e é verificado se existe o sobrenome 'silva' dentro de cada palavra que está no  string nome
recebida na entrada.
"""
