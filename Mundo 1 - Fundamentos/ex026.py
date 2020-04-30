# Exercício Python #026 - Primeira e última ocorrência de uma string

frase = str(input('\033[1;30mDigite uma frase: ').strip()).upper()
a = frase.count('A')
# Somei 1 ao find porque a contagem dos caracteres começa a partir do 0 no python.
pv = frase.find('A') + 1
# Como ele mostra -1 quando a letra não é encontrada então ele se torna 0 nesse caso.
uv = frase.rfind('A') + 1
print('\n\033[1;31mQuantas vezes a letra A aparece na frase: {}.'.format(a))
print('\033[1;36mPosição em que a letra A aparece pela primeira vez na frase: {}.'.format(pv))
print('\033[1;35mPosição em que a letra A aparece pela última vez na frase: {}.'.format(uv))

"""
Com relação aos comentários em #
Como um cara comentou: no programa, o primeiro índice é 0, você coloca o +1 para o usuário, para ele é posição 1.
"""


frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
