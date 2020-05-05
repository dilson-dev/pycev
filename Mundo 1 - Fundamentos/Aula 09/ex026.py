# Exercício Python #026 - Primeira e última ocorrência de uma string

"""
DESAFIO 026
Faça um programa que leia uma frase pelo teclado e mostre:
► Quantas vezes aparece a letra "A";
► Em que posição ela aparece a primeira vez;
► Em que posição ela aparece a última vez.
"""

frase = str(input('\033[1;30mDigite uma frase: ').strip()).upper()
a = frase.count('A')

# Somado 1 ao find e rfind porque a contagem dos caracteres começa a partir do 0 no Python.
# E como ele mostra -1 quando o caractere não é encontrado então ele se torna 0 nesse caso.

pv = frase.find('A') + 1
uv = frase.rfind('A') + 1

print('\n\033[1;31mQuantas vezes a letra A aparece na frase: {}.'.format(a))
print('\033[1;36mPosição em que a letra A aparece pela primeira vez na frase: {}.'.format(pv))
print('\033[1;35mPosição em que a letra A aparece pela última vez na frase: {}.'.format(uv))

"""
No programa, o primeiro índice é 0, é somada 1 para mostrar ao usuário, pois para ele é posição 1.
"""


# Mais resumido:
"""
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
"""
