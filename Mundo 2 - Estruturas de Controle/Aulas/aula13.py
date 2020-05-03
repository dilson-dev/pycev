# Curso Python #013 - Estrutura de repetição for


#  for r in range(-100, 201, 10):
#   print(r)
n = int(input('Digite um número inteiro para ver sua tabuada: '))
for r in range(0, n * 10 + 1, n):
    print(r)
print('\nFim.')

soma = 0
primeiro = int(input('\nPrimeiro elemento: '))
ultimo = int(input('Último elemento: '))
passo = int(input('Passo: '))
for c in range(primeiro, ultimo + 1, passo):
    valor = int(input('Valor: '))
    soma += valor
print('A soma de todos os elementos é: {}.'.format(soma))
