# Exercício Python #054 - Grupo da Maioridade
# Análise Nascimentos

from datetime import date
ano_atual = date.today().year
pessoas = int(input('\nQuantidade de pessoas a ser verificado o nascimento: '))
nomeMenores = []
nomeMaiores = []
nascimentoMaiores = []
nascimentoMenores = []
for c in range(pessoas):
    nome = input(f'\nNome: ')
    nascimento = int(input(f'Data de nascimento: '))
    if ano_atual - nascimento >= 21:
        nomeMaiores += [nome]
        nascimentoMaiores.append(nascimento)
    elif ano_atual - nascimento < 21:
        nomeMenores += [nome]
        nascimentoMenores.append(nascimento)

print('\nMenores de idade:')
for c in range(len(nascimentoMenores)):
    print(f'Nome: {nomeMenores[c]}. Data de nascimento: {nascimentoMenores[c]}')

print('\nMaiores de idade')
for c in range(len(nascimentoMaiores)):
    print(f'Nome: {nomeMaiores[c]}. Data de nascimento: {nascimentoMaiores[c]}.')

print(f'\nMenores de idade: {len(nascimentoMenores)}.\nMaiores de idade: {len(nascimentoMaiores)}.')

'''
from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
print('\n\033[1mAnálise maioridade 21 anos\033[m\n')
for pessoa in range(7):
    nascimento = int(input(f'Em que ano a {pessoa + 1}ª pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:  # (ano_atual - nascimento) < 21:
        menores += 1
print(f'\nMaiores de idade: {maiores}.\nMenores de idade: {menores}.')
'''
