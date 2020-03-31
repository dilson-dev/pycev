n1 = int(input('\n\033[31mDigite um número: '))
n2 = int(input('\033[32mDigite outro número: \033[m'))
s = n1 + n2
print('\nA soma entre \033[31m{0}\033[m e \033[32m{1}\033[m é \033[1;35m{2}\033[m.'.format(n1, n2, s))
# Tanto faz se {} ou {0}, pois o .format segue a sequência colocada nas chaves na hora de substituir os valores.
