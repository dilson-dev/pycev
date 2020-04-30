# Exercício Python #089 - Boletim com listas compostas
"""
DESAFIO 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada dado individualmente.
"""
boletim = list()
print()
while True:
    print('-=' * 15)
    nome = input('Nome: ')
    while True:
        notas = [float(input(f'Nota {i}: ')) for i in range(1, 3)]
        if 0 <= notas[0] <= 10 and 0 <= notas[1] <= 10:
            media = sum(notas) / len(notas)
    boletim.append([nome, notas, media])
    print('-=' * 15)
    res = ''
    while res == '' or res[0] not in 'SN':
        res = input('Quer continuar? [S/N] ').strip().upper()
    if res[0] == 'N':
        break

print('', '–' * 30, f'|{"BOLETIM":^28}|', '–' * 30, sep='\n')
print(f'| Nº {"Nome":<11} {"Média":>11} |', '–' * 30, sep='\n')
for numero, dado in enumerate(boletim):
    print(f'| {numero:<3} {dado[0]:<17}{dado[2]:^5.1f} |')
print('–' * 30, '\n')

while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if n == 999:
        break
    for numero, dado in enumerate(boletim):
        if numero == n:
            print(
                '–' * 45, f'Notas de {dado[0]} são {dado[1]}.', '–' * 45, sep='\n')

print('\nFINALIZANDO...\n<<< Volte sempre! >>>')
