# Exercício Python #023 - Separando dígitos de um número
"""
num = str(input('Digite um número com até 4 digitos de 0 a 9999: '))
unidade = num[-1]
dezena = num[-2]
centena = num[-3]
milhar = num[-4]
print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
"""

# Código comentários funcional sem complicações
num = '000' + str(input('Informe um número: ')).strip()
print('Unidade: {}'.format(num[-1]))
print('Dezena: {}'.format(num[-2]))
print('Centena: {}'.format(num[-3]))
print('Milhar: {}'.format(num[-4]))


'''
num = str(input('Informe um número: '))
n = str(num)
print('Analisando o número {}.'.format(num))
print('Unidade: {}.'.format(n[-1]))
print('Dezena: {}.'.format(n[-2]))
print('Centena: {}.'.format(n[-3]))
print('Milhar: {}.'.format(n[-4]))
'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\n\033[1;30mAnalisando o número \033[4;30m{}'.format(num))
print('\033[1;34mUnidade: {}'.format(u))
print('\033[1;31mDezena: {}'.format(d))
print('\033[1;32mCentena: {}'.format(c))
print('\033[1;36mMilhar: {}'.format(m))
