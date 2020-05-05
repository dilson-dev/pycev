# Exercício Python #054 - Grupo da Maioridade

"""
DESAFIO 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""


# Minha solução com quantidade de pessoas para analisar conforme entrada do usuário, listas e pedindo os nomes:

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


# Solução conforme o vídeo:
'''
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0
print('\n\033[1mAnálise maioridade 21 anos\033[m\n')
for pessoa in range(1, 8):  # range(7) (0, 7)
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:  # idade < 21:
        menores += 1
print(f'\nMaiores de idade: {maiores}.\nMenores de idade: {menores}.')
'''
