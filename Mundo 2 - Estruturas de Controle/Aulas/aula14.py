# Curso Python #014 - Estrutura de repetição while

"""for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'  # Pequena gambiarra para iniciar a estrutura de repetição while
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')"""

n = 1  # Gambiarra
par = impar = 0

# É possível definir múltiplas variáveis com mesmo valor assim, só não ajuda muito em relação a dicionários, e listas.
# Nesses casos é assimilado o valor ao objeto, e ao mudar o valor de um dicionário/lista muda os outros definidos juntos.


while n != 0:  # Gambiarra
    n = int(input('Digite um valor: '))
    if n != 0:  # Condição parecida com while
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'\nQuantidade de números pares digitados: {par}.\nQuantidade de números ímpares digitados: {impar}.')
