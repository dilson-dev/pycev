# Exercício Python #046 - Contagem regressiva
# Contagem Regressiva com For

from time import sleep
from emoji import emojize
from playsound import _playsoundWin

'''
print('\n\033[1;30mContagem regressiva para o estouro dos fogos de artíficio.\033[m\n')
for c in range(10, -1, -1):
    sleep(1), print(c)
print('\n\033[1;33mBOOM, POW, PA, PE, (...)!\033[1;35m', end='      ')
for r in range(10):
    print(emojize(':fireworks:       '), end='')
print()
'''

'''print('\n\033[1;33mContagem regressiva para o trem partir:\n\033[m')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\n\033[1;34mPartindo (...)!\033[m', end='      ')

print(emojize(':suspension_railway:') * 20)
print(' ' * 20, '▔' * 22)'''

print('\n\033[1;33mContagem regressiva para o lançamento do foguete:\n\033[m')

print('''[ 1 ] Texto;
[ 2 ] Áudio.''')
opcao = 0
while opcao != 1 and opcao != 2:
    opcao = int(input('\nOpção: '))
    if opcao != 1 and opcao != 2:
        print('\nErro, tente novamente.')
print()
if opcao == 1:
    for c in range(10, -1, -1):
        sleep(1), print(c)
    print('\n\033[1;34mDecolando (...)!\033[m\n')
else:
    _playsoundWin('ex046.mp3')  # Efeito de som de Nave Decolando

print(' ' * 10, emojize(':new_moon:'), '\n\n\n')
print(' ', emojize(':rocket:'))
