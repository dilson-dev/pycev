"""
DESAFIO 083
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
'''
exp = input('\nDigite uma expressão: ').strip()

print()

parenteses = []
nparenteses = []

for char in exp:
    if char in '()':
        parenteses += char
    else:
        nparenteses += char

if not parenteses or not nparenteses:
    print('Expressão deve ter parênteses e caracteres.')
else:
    start = 0
    if parenteses.count('(') == parenteses.count(')'):  # Analisa a quantidade de parênteses
        for p in parenteses:  # Analisa a ordem dos parênteses
            if p == '(' and ')' in parenteses[start::]:
                start += parenteses[start::].index(')') + 1
    print('Expressão ', 'válida' if start == len(parenteses) else 'inválida', '!', sep='')
    '''
'''  # Sem o método count
expv = False
starta = startf = 0
for pos, p in enumerate(parenteses):
    if p == '(' and ')' in parenteses[starta::]:
        starta += parenteses[starta::].index(')') + 1
    elif p == ')' and '(' in parenteses[startf:pos]:
        startf += parenteses[startf:pos].index('(') + 1
    else:
        expv = False
        break
print('Expressão ', 'válida' if expv else 'errada', '!', sep='')
'''

'''  # Solução baseada num comentário que vi no YouTube
parentesesAF = 0
for p in parenteses:
    parentesesAF += 1 if p == '(' else -1
    if parentesesAF < 0:
        break
print('Expressão ', 'errada' if parentesesAF else 'válida', '!', sep='')
'''

# Solução do Guanabara
expressao = input('\nDigite a expressão: ')
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha):  # len(pilha) > 0
            pilha.pop()
        else:
            pilha.append(')')
            break

print(len(pilha))
print('\nExpressão ', 'válida' if len(pilha) == 0 else 'errada', '!', sep='')
# 'válida' if not len(pilha) | 'errada' if len(pilha)
