# Exercício Python #093 - Cadastro de Jogador de Futebol

"""
DESAFIO 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = dict()

jogador['Nome'] = input('\nNome do jogador: ').capitalize().strip()

partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

jogador['Gols'] = [int(input(f'   Quantos gols na {num + 1}ª partida? ')) for num in range(partidas)]

jogador['Total'] = sum(jogador['Gols'])

# Adicionei a média de gols por partida, pois achei que é uma informação legal de ver também:
jogador['Média'] = round(jogador['Total'] / partidas, 2)

print('-=' * 35)

print(jogador)

print('-=' * 35)

[print(f'{k} = {v}') for k, v in jogador.items()]

print('-=' * 35)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
[print(f'     => Na {num}ª partida fez {gol} gol(s).') for num, gol in enumerate(jogador['Gols'], 1)]

# Outra maneira de fazer a linha acima:
# [print(f'     => Na {num + 1}º partida fez {jogador['Gols'][num]} gols.') for num in range(partidas)]

print(f'\n{jogador["Nome"]} fez {jogador["Total"]} gol(s) no total.')

# Adicional:
print(f'\n{jogador["Nome"]} tem uma média de {jogador["Média"]} gol(s) por partida.')

if jogador['Média'] >= 2:
    print(f'\n{jogador["Nome"]} é um jogador de alto nível!')
elif jogador['Média'] >= 1:
    print(f'\n{jogador["Nome"]} é um excelente jogador.')


# Conforme solução do vídeo:
'''
jogador, partidas = dict(), list()
jogador['Nome'] = input('\nNome do jogador: ')
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(total):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
'''
