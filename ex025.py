"""
nome = str(input('Digite o seu nome completo: '))
silva = 'Silva' in nome
print('Tem ´Silva` em seu nome? {}.'.format(silva))
"""

nome = str(input('\033[1;30mqual é o seu nome completo? ')).strip()
print('\033[1;34mSeu nome tem \"Silva\"? {}.'.format('silva' in nome.lower().split()))

"""
Nesse caso ele procura na lista, pois nome gera uma lista com split, assim se tiver silvana ele considera false.
"""
