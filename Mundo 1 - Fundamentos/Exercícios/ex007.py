# Exercício Python #007 - Média Aritmética
n1 = float(input('\033[1;30mDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: \033[m'))
m = (n1 + n2)/2
if m >= 7:
    corm = '\033[1;32m'  # corm = cor da média 32 - verde, 31 - vermelho
else:
    corm = '\033[1;31m'
print('\nA \033[1;34mmédia\033[m entre \033[35m{}\033[m e \033[35m{}\033[m é {}{:.1f}\033[m.'.format(n1, n2, corm, m,))
