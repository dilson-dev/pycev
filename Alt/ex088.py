from random import sample
from time import sleep
qtdjogos = int(input('\nQuantos jogos quer sortear? '))
jogos = [sorted(sample(range(1, 61), 6)) for i in range(qtdjogos)]
for n, jogo in enumerate(jogos):
    sleep(1), print(f'Jogo {n:>2} = [{", ".join(f"{valor:>2}" for valor in jogo)}].')

'''
from random import sample

print('\nNão repete sequências\n')
qt, nums, conjunto = 5, [], set()

while len(conjunto) < 5:
    conjunto.add(tuple(sorted(sample(range(10), 2))))

[print(i, sorted(j)) for i, j in enumerate(conjunto, 1)]


print('\nRepete sequências\n')

conjunto.clear()

conjunto = []

for n in range(5):
    conjunto.append(tuple(sorted(sample(range(10), 2))))

[print(i, sorted(j)) for i, j in enumerate(conjunto, 1)]
'''
