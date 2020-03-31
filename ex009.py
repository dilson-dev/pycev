# Tabuada

c = {'bf': '\033[1;30m',  # Branco forte
     'vermf': '\033[1;31m',  # Vermelho forte
     'am': '\033[33m',  # Amarelo
     'azft': '\033[1;34m',  # Azul forte
     'rf': '\033[1;35m',  # Roxo/rosa forte
     'l': '\033[m'}  # Limpar

n = int(input('{}Digite um número: '.format(c['am'])))
print('\n{} Tabuada do número {}\n'.format(c['azft'], n))
print('\033[1m' + '-' * 12)
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 0, c['rf'], c['vermf'], n * 0))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 1, c['rf'], c['vermf'], n * 1))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 2, c['rf'], c['vermf'], n * 2))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 3, c['rf'], c['vermf'], n * 3))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 4, c['rf'], c['vermf'], n * 4))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 5, c['rf'], c['vermf'], n * 5))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 6, c['rf'], c['vermf'], n * 6))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 7, c['rf'], c['vermf'], n * 7))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 8, c['rf'], c['vermf'], n * 8))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 9, c['rf'], c['vermf'], n * 9))
print('{}{} x {:2} {}= {}{}'.format(c['bf'], n, 10, c['rf'], c['vermf'], n * 10))
print('\033[1m' + '-' * 12)
