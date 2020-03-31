from math import hypot
co = float(input('\033[1;30mComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('\nA hipotenusa medirá {}{:.2f}{}.'.format('\033[1;35m', h, '\033[1;30m'))
