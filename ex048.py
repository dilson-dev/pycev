"""
for c in range(0, 500, 3):
    if c % 2 != 0:
        s += c
print(s)
"""
'''for c in range(1, 500, 2):# range(1, 501, 2), porém 500 é par, ou seja, não precisa incluir na contagem.
    r += 1
    if c % 3 == 0:
        s += c
        v += 1

print(r, v, s)
r = 0
s = 0
v = 0
'''

'''for c in range(3, 500, 6):
    s += c
    v += 1
print('\nA soma de todos os\033[1;34m', v, '\033[mvalores solicitados é:\033[1;32m', str(s) + '\033[m.')'''

print()
print('=-' * 33)
print('| Soma números ímpares de um número ímpar, no intervalo desejado |')
print('=-' * 33)

num = 0
while num % 2 == 0:
    print()
    num = int(input('Número ímpar: '))
    if num % 2 == 0:
        print('Erro, tente novamente.')

intervalo = int(input('\nIntervalo: '))

nums = [i for i in range(num, intervalo + 1, num * 2)]

print('\nA soma de todos os\033[1;34m', len(nums), '\033[mvalores solicitados é\033[1;32m', str(sum(nums)) + '\033[m.')
