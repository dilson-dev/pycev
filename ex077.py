"""
DESAFIO 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.
"""

alfabeto = ()
for i in range(65, 91):
    alfabeto += chr(i),

# Pega input do usuário identificando se está no alfabeto, se não está, pede novamente o input.
while True:
    repeticao = False
    frase = input('\nDigite uma frase/palavras sem acentos: ').strip().upper()
    palavras = frase.split()
    for palavra in palavras:
        for letra in palavra:
            if letra not in alfabeto:
                repeticao = True
                break
        if repeticao:
            break
    if not repeticao:
        break
    print('Erro, você digitou um acento/símbolo. Tente novamente.')

# Escreve as vogais da palavra na tela
for palavra in palavras:
    print(f'\nVogais de {palavra}:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print()

'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
'''