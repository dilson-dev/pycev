# Exercício Python #093 - Cadastro de Jogador de Futebol

"""
DESAFIO 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

nome = input('\nNome do jogador: ').capitalize().strip()
partidas = int(input(f'Quantas partidas {nome} jogou? '))

print()

gols = []

[gols.append(int(input(f'Quantos gols na {num}º partida? '))) for num in range(1, partidas + 1)]

jogador = {'Nome': nome, 'Gols': gols, 'Total': sum(gols)}

print('-=' * 35)
print(jogador)
print('-=' * 35)

[print(f'{k} = {v}') for k, v in jogador.items()]

print('-=' * 35)

[print(f'     => Na {num}º partida fez {gol} gol(s).') for num, gol in enumerate(gols, 1)]
# [print(f'     => Na {num + 1}º partida fez {gols[num]} gols.') for num in range(partidas)]

print(f'\n{nome} fez {sum(gols)} gol(s) no total.')

print(f'\n{nome} tem uma média de {(sum(gols) / len(gols)):.1f} gol(s) por partida.')

# mediagols = sum(gols) / len(gols)
# if mediagols >= 2:
#     print(f'\n{nome} é um jogador de alto nível!')
# elif mediagols >= 1:
#     print(f'\n{nome} é um jogador bom.')
# elif mediagols != 0:
#     print(f'\n{nome} se for atacante precisa melhorar!')
# else:
#     print(f'\n{nome} é provavelmente um goleiro, ou focado na defesa, caso contrário precisa melhorar.')
