boletim = []
print()
while True:
    nome = input(f'{"-=" * 15}\nNome: ')
    while True:
        notas = [float(input(f'Nota {i}: ')) for i in range(1, 3)]
        if 0 <= notas[0] <= 10 and 0 <= notas[1] <= 10:
            media = sum(notas) / len(notas)
            break
    boletim.append([nome, notas, media])
    print('-=' * 15)
    continuar = ''
    while continuar == '' or continuar[0] not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar[0] == 'N':
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
