# Exercício Python #062 - Super Progressão Aritmética v3.0

"""
DESAFIO 062
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
"""


"""
primeiroTermo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))

ultimoTermo = primeiroTermo + (razao * 9)

termo = c = 0

print()

while termo < ultimoTermo:
    termo = primeiroTermo + (razao * c)
    print(f'{c + 1}º \033[1;32m{termo}\033[m', end=' → ')
    c += 1
print('Acabou.')

res = ''
while res != 'S' and res != 'N':
    res = input('\nDeseja mostrar outros termos? [S/N] ').upper()
    if Res != 'S' and Res != 'N':
        print('Erro, tente novamente.')

if res == 'S':
    numtermos = 1

    while numtermos != 0:
        numtermos = int(input('\nQuantos termos (0 para sair): '))

        ultimoTermo = (termo + razao) + (razao * numtermos)
        if numtermos != 0:
            while (termo + razao) < ultimoTermo:
                termo = primeiroTermo + (razao * c)
                print(f'{c + 1}º \033[1;32m{termo}\033[m', end=' → ')
                c += 1
            print('Acabou.')
        '''
        if numtermo > 0:
            termo = primeiroTermo + (razao * (numtermo - 1))
            print(f'{numtermo}º termo = {termo}')
        '''
"""

print('-=' * 10)
print(f'|{"Gerador de PA":^18}|')
print('-=' * 10)

primeiroTermo = int(input('\nPrimeiro termo da PA: '))
razao = int(input('Razão: '))

# ultimoTermo = primeiroTermo + (razao * 9)

termo = primeiroTermo
c = 0

numtermos = 10

while c < numtermos:
    print(termo, end=' → ')
    termo += razao
    c += 1
    if c == numtermos:
        print('PAUSA')
        numtermos += int(input('\nQuantos termos a mais você quer mostrar? '))
print(f'\nProgressão finalizada c/ {numtermos} termos mostrados.')

'''while c < 10:  # termo < ultimoTermo
    print(termo, end=' → ')
    termo += razao
    c += 1
print('PAUSA')

totTermos = 10

numtermos = 1

while numtermos > 0:
    numtermos = int(input('\nQuantos termos a mais você quer mostrar? '))
    c = 0
    while c < numtermos:
        print(termo, end=' → ')
        termo += razao
        c += 1
    totTermos += numtermos
    print('PAUSA')
print(f'\nProgressão finalizada com {totTermos} termos mostrados.')'''
