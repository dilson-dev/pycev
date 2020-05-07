# Exercício Python #090 - Dicionário em Python

"""
DESAFIO 090
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
# aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 7 else 'Reprovado'
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:  # 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 30)
[print(f'  - {k} é {v}.') for k, v in aluno.items()]

# for k, v in aluno.items():
#     print(f'{k} é {v}.')
