# Exercício Python #027 - Primeiro e último nome de uma pessoa

"""
DESAFIO 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.
Ex:
Input - Ana Maria de Souza
Output - Primeiro = Ana; Último = Souza
"""

nome = (str(input('Digite o seu nome completo: ')).strip()).split()
primeiro = nome[0]
ultimo = nome[-1]
print('\n{}Primeiro nome: {}.'.format('\033[1;33m', primeiro))
print('{}Último nome: {}.'.format('\033[1;34m', ultimo))

'''
O [-1] seria como uma 'contração' de [len() - 1].
O 'len' contabiliza o número total de elementos de uma determinada lista dentro do parênteses começando do 1, assim se uma
lista tem n elementos ele irá resultar em n. Já na lista a contagem começa do 0.
Diminuindo o número contado pelo len em 1 você obtém o último elemento de uma lista qualquer.

Supomos que existe uma variável lista que tem 4 elementos, ao utilizar len(lista) ele irá resultar em 4.
Levando em consideração que o Python inicia a contagem dos elementos do 0 e a lista do 1, há uma diferença de 1, então ao
diminuir essa contagem da lista feita pelo len(4) da contagem de elementos feita pelo Python você obtém o último elemento.
4 - 1 = 3 == Python(0, 1, 2, >3<).
'''


n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))
