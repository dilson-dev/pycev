ni = str(input('\033[1;30mQual o seu nome completo? '))
d = ni.split()  # ns = ni.strip()
n = ' '.join(d)
ma = n.upper()
mi = n.lower()
le = len(''.join(d))
le1 = len(d[0])
print('\n\033[1;31mMaíusculo: {}\n\033[1;36mMinúsculo: {}\n\033[1;34mLetras: {}'.format(ma, mi, le))
print('\033[1;35mLetras do primeiro nome: {}'.format(le1))


nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # (''.join(nome.split()))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

"""
nome = str(input('Digite seu nome completo: '))
ns = nome.split()  # Não usei strip, pois o split já resolveu o strip e os espaços entre as letras.
nj = ' '.join(ns)
ma = nj.upper()
mi = nj.lower()
le = len(''.join(ns))
pn = ns[0]
le1 = len(pn)
print('Analisando seu nome...\nSeu nome em maiúsculas é {}.\nSeu nome em minúsculas é {}.'.format(ma, mi))
print('Seu nome tem ao todo {} letras.\nSeu primeiro nome é {} e ele tem {} letras.'.format(le, pn, le1))
"""
