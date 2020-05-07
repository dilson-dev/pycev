# Exercício Python #095 - Aprimorando os Dicionários

"""
DESAFIO 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.
"""

jogadores = []
repetir = 'S'
while repetir == 'S':
    print('-' * 30)
    jogador = ({'nome': input('Nome do jogador: ').capitalize().strip(),
                'gols': [int(input(f'Gols {n + 1}ª partida: ')) for n in range(int(input('Partidas jogadas: ')))]})
    jogador.update({'total': sum(jogador['gols'])})
    jogadores.append(jogador)  # jogadores.append(jogador.copy())
    repetir = ''
    print('-' * 30)
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('Cadastrar outro jogador? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('Digite S para Sim e N para Não.')

print('-=' * 30)

# print(jogadores)

# print(f'| Registro Nome Gols Total')

for n, j in enumerate(jogadores):

    # Cria descrição da tabela
    if n == 0:

        print(f'| {"cod":<3}', end=' ')
        for k in j.keys():
            print(f'| {k:^10}', end='')
        print(' |\n', '-' * 44, sep='')

    # Imprime informação de cada jogador
    print(f'|{n:^4}', end=' ')
    for v in j.values():
        if not isinstance(v, list):
            print(f'| {str(v):^10}', end='')
        else:
            print(f'| {(" ".join(str(va) for va in v)):^10}', end='')
    print(' |')
num = 0
while num != 999:
    print('-' * 44)
    num = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    # 1ª solução para mostrar dados usando as funções range e len:
    if num in range(len(jogadores)):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}:')
        for jogo, gol in enumerate(jogadores[num]['gols'], 1):
            print(f'   No {jogo}º jogo fez {gol} gol(s).')
    elif num != 999:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')

    # 2ª solução c/ Try Except:
    '''
    try:
        assert num >= 0
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}')
        for jogo, gol in enumerate(jogadores[num]['gols'], 1):
            print(f'   No jogo {jogo} fez {gol} gols.')
    except:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')
    '''

    # 3ª solução usando for else e break:
    '''
    for n, j in enumerate(jogadores):
        if num == n:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[num]["nome"]}')
            for jogo, gol in enumerate(jogadores[num]['gols'], 1):
                print(f'   No jogo {jogo} fez {gol} gols.')
            break
    else:
        print(f'\nERRO! Não existe jogador com código {num}! Tente novamente.')
    '''


print('\n<< VOLTE SEMPRE >>')
