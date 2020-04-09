"""
DESAFIO 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
from statistics import mean

boletim = list()
dados = []

print()
while True:
    print('-=' * 15)
    dados.append(str(input('Nome: ')))
    while True:
        dados.append([float(input(f'Nota {i}: ')) for i in range(1, 3)])  # f'{i}ª nota: '
        if 0 <= dados[1][0] <= 10 and 0 <= dados[1][1] <= 10:
            dados.append(mean(dados[1]))  # sum(aluno[1]) / len(aluno[1])  # 2
            break
        dados.pop()
    boletim.append(dados[:])
    print('-=' * 15)
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break
    dados.clear()

print(), print('–' * 30)
print(f'|{"BOLETIM":^28}|')
print('–' * 30)
print(f'| Nº {"Nome":<13} {"Média":>9} |')
print('–' * 30)
for numero, aluno in enumerate(boletim):
    print(f'| {numero:<2} {aluno[0]:<18}{aluno[2]:^5.1f} |')
print('–' * 30, '\n')

while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if n == 999:
        break
    print('–' * 45)
    for numero, dado in enumerate(boletim):
        if numero == n:
            print(f'Notas de {dado[0]} são {dado[1]}.')
    print('–' * 45)

print('\nFINALIZANDO...')
print('<<< Volte sempre! >>>')
