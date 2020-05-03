# Exercício Python #023 - Separando dígitos de um número
from math import radians, sin, cos, tan
a = float(input('\n\033[1;36mDigite um ângulo qualquer: \033[m'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('\nO ângulo \033[1;36m{}\033[m tem:'.format(a))
print('\nSENO de \033[1;35m{:.2f}\033[m.'.format(s))
print('COSSENO de \033[1;31m{:.2f}\033[m.'.format(c))
print('TANGENTE de \033[1;33m{:.2f}\033[m.'.format(t))
