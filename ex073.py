"""
DESAFIO 073
Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""

anos = (2014, ('Cruzeiro', 'São Paulo', 'Internacional', 'Corinthians', 'Atlético Mineiro',
               'Fluminense', 'Grêmio', 'Athletico-PR', 'Santos', 'Flamengo', 'Sport Recife',
               'Goiás', 'Figueirense', 'Coritiba', 'Chapecoense','Palmeiras', 'Vitória',
               'Bahia', 'Botafogo', 'Criciúma'),
        2015, ('Corinthians', 'Atlético Mineiro', 'Grêmio', 'São Paulo', 'Internacional',
               'Sport Recife', 'Santos', 'Cruzeiro', 'Palmeiras', 'Athletico-PR',
               'Ponte Preta', 'Flamengo', 'Fluminense', 'Chapecoense', 'Coritiba',
               'Figueirense', 'Avaí', 'Vasco da Gama', 'Goiás', 'Joinville'),
        2016, ('Palmeiras', 'Santos', 'Flamengo', 'Atlético Mineiro', 'Botafogo',
               'Athletico-PR', 'Corinthians', 'Ponte Preta', 'Grêmio', 'São Paulo',
               'Chapecoense', 'Cruzeiro', 'Fluminense', 'Sport Recife', 'Coritiba',
               'Vitória', 'Internacional', 'Figueirense', 'Santa Cruz', 'América-MG'),
        2017, ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
               'Vasco da Gama', 'Chapecoense', 'Atlético Mineiro', 'Botafogo',
               'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
               'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goianiense'),
        2018, ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
               'Atlético Mineiro', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
               'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
               'Vasco da Gama', 'Sport Recife', 'América-MG', 'Vitória', 'Paraná'),
        2019, ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
               'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
               'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará',
               'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'))

while True:
    while True:
        ano = int(input('\nEscreva o ano que deseja ver a tabela do brasileirão de 2014 a 2019: '))
        if ano in anos:
            break
        print('Erro, tente novamente.')

    times = anos[anos.index(ano) + 1]

    while True:
        timeUser = input('\nEscreva o time que deseja saber a posição na tabela: ').strip().lower().capitalize()
        if timeUser in times:
            break
        print(f'Erro, tente novamente. O time {timeUser} não está na tabela.')

    print()
    print('=' * 40)
    print(f'|{"Tabela Brasileirão Série A " + str(ano):^38}|')
    print('=' * 40)
    print(f'| {"Posição":^7} | {"Time":^26} |')
    print('=' * 40)
    for pos, time in enumerate(times):
        print(f'| {pos + 1:^7} | {time:^27}|')
    print('=' * 40)

    print()

    print(f'5 primeiros colocados do brasileirão {ano}: {times[:5]}')
    print(f'4 últimos colocados: {times[-4:]}.')  # times[16:]
    print(f'Times em ordem alfabética: {sorted(times)}')
    print(f'Posição do time {timeUser} na tabela: {times.index(timeUser) + 1}º')

    res = ''
    while res not in 'SN' or res == '':
        res = input('\nQuer refazer o programa? [S/N] ').strip().upper()[0]
        if res in 'SN' and res != '':
            break
        print('Erro, tente novamente.')

    if res == 'N':
        break
