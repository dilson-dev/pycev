#

"""
DESAFIO 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

jogadores = []
repetir = 'S'
while repetir == 'S':
    print('-' * 25)
    jogador = ({'nome': input('Nome do jogador: ').capitalize().strip(),
                'gols': [int(input(f'Gols {n + 1}ª partida: ')) for n in range(int(input('Partidas jogadas: ')))]})
    jogador.update({'total': sum(jogador['gols'])})
    jogadores.append(jogador)  # jogadores.append(jogador.copy())
    repetir = ''
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('\nQuer cadastrar outro jogador? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('Digite S para Sim e N para Não.')

print('-=' * 35)

# print(f'| Registro Nome Gols Total')

for k in jogadores[0].values():


for n, j in enumerate(jogadores):
    for k, v in j.items():
        print()
