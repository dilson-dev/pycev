#
"""
DESAFIO 090
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 7 else 'Reprovado'
print()
[print(f'{k} é {v}.') for k, v in aluno.items()]

# for k, v in aluno.items():
#     print(f'{k} é {v}.')
