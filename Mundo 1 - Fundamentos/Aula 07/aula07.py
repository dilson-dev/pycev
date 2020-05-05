# Curso Python #07 - Operadores Aritméticos

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2  # Soma
m = n1 * n2  # Multiplacação
d = n1 / n2  # Divisão
di = n1 // n2  # Divisão Inteira
e = n1 ** n2  # Exponenciação
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}.'.format(di, e))
#  \n para quebrar linha e end=' ' vazio para não quebrar no final, mas ' ' pode ser
#  substituído por qualquer outra coisa que quiser colocar entre os prints.

# Existe também o resto da divisão com % e subtração com -
