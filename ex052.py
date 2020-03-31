# Números Primos

# 1, 3, 7, 9
# Após número 9, tod0 número que tem o último algarismo diferente destes não é primo

print('''
Analisador números primos:

[ 1 ] Apenas um número;
[ 2 ] Uma sequência com início e fim.''')
opcao = 0
while opcao != 1 and opcao != 2:
    opcao = int(input('\nOpção: '))
    if opcao != 1 and opcao != 2:
        print('Erro. Tente novamente.')

if opcao == 1:
    numero = int(input('\nDigite um número: '))
    divisores = []
    print()
    if numero > 1:
        for c in range(numero):
            divisores += [(c + 1) for i in [numero] if i % (c + 1) == 0]
            '''if numero % (c + 1) == 0: 
                divisores.append(c + 1)'''

        print('\nDivisores de \033[1;32m' + str(numero) + '\033[m:', divisores)
        print(f'Total:{len(divisores)}.')

        if len(divisores) > 2:
            print('Não é primo.')
        else:
            print('É primo')
    elif numero == 0 or numero == 1:
        print('Zero (0) e Um (1) não são primos e nem compostos.')
    else:
        print('Números negativos não se encaixam na exigência de um número primo, portanto não são primos.')
else:
    inicio = 0
    fim = 0
    while inicio > fim or inicio < 2:
        inicio = int(input('\nInício: '))
        fim = int(input('Fim: '))
        if inicio > fim or inicio < 2:
            print('\nErro. Tente novamente.')
    for num in range(inicio, fim + 1):
        divisores = []
        for c in range(num):
            divisores += [(c + 1) for i in [num] if i % (c + 1) == 0]

        print('\nDivisores de \033[1;32m' + str(num) + '\033[m:', divisores)
        print('Total:', len(divisores))

        if len(divisores) == 2:
            print('É primo.')
        else:
            print('Não é primo')

'''
numero = int(input('\nDigite um número: '))
divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[1;32m{c}', end=' ')
        divisores += 1
    else:
        print(f'\033[1;31m{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {divisores} vezes.\nE por isso ele \033[1m', end='')
if divisores == 2:
    print('É PRIMO.')
else:
    print('NÃO É PRIMO.')
'''
