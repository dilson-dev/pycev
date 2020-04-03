"""
DESAFIO 083
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

exp = input('\nDigite uma expressão: ')

listexp = []

for char in exp:
    listexp.append(char)

contpaberto = listexp.count('(')
contpfechado = listexp.count(')')

print()

if contpaberto == contpfechado == 0:
    print('Nenhum parênteses na expressão, portanto é válida.')
elif contpaberto == contpfechado:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
