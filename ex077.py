"""
DESAFIO 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.
"""

alfabeto = ()

vogais = ('A', 'E', 'I', 'O', 'U')

for i in range(65, 91):
    alfabeto += chr(i),

while True:
    repeticao = 0
    frase = input('\nDigite uma frase/palavras sem acentos: ').strip().upper()
    palavras = frase.split()
    for palavra in palavras:
        for letra in palavra:
            if letra not in alfabeto:
                repeticao += 1
    if repeticao == 0:
        break

    print('Erro, você digitou um acento/símbolo. Tente novamente.')

for palavra in palavras:
    print(f'\nVogais de {palavra}:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')

print()
