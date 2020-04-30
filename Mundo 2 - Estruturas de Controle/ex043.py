# Exercício Python #043 - Índice de Massa Corporal
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (metros):  '))
imc = peso / (altura ** 2)  # Parênteses desnecessários (Ordem de precedência).
print('\nIMC = {:.1f}\nCondição: \033[1;30m'.format(imc), end='')
if imc < 18.5:
    p = 'Abaixo do peso'
elif imc < 25:
    p = 'Peso ideal'
elif imc < 30:
    p = 'Sobrepeso'
elif imc < 40:
    p = 'Obesidade'
else:
    p = 'Obesidade mórbida\033[1;31m\n\nCondição de risco! Tome cuidado.'
print(p)
