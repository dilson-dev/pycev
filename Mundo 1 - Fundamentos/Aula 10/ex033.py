# Exercício Python #033 - Maior e menor valores

"""
DESAFIO 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print()
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('\033[1;35mO maior número é {}.'.format(maior))
print('\033[1;36mO menor número é {}.'.format(menor))


# Solução dos comentários sem usar condições, através de listas e funções que pegam o maior e menor valor:
"""
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))
"""


# Solução apresentada no vídeo:
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
'''
