# Exercício Python #055 - Maior e menor da sequência
# Análise Pesos

peso_ma = 0
peso_me = 0  # peso_me = 1000 (Gambiarra substituída pelo acréscimo nas condições)

print()
for p in range(5):
    peso = float(input(f'Digite o peso da {p + 1}ª pessoa: '))
    '''
    if p == 0:
        peso_me = peso
        peso_ma = peso
    '''
    if peso > peso_ma or p == 0:  # p == 0 → Comparação para saber se é a primeira repetição.
        peso_ma = peso
    if peso < peso_me or p == 0:  # Caso sim, o valor em peso é definidido como o maior e menor.
        peso_me = peso
print('\nO menor peso lido foi {}Kg e o maior foi {}Kg.'.format(peso_me, peso_ma))
