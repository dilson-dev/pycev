# Exercício Python #053 - Detector de Palíndromo
# Análise Palíndromos e Capicuas

print('''
    \033[1mVerificar:\033[m\n
    [1] Palíndromos;
    [2] Capicuas.
''')
opcao = 0
while opcao != 1 and opcao != 2:
    opcao = int(input('Digite a opção desejada: '))
    if opcao != 1 and opcao != 2:
        print('\nErro, tente novamente.')
print()
if opcao == 1:
    # Desconsiderando acentos e espaços
    frase = ''.join(str(input('Digite uma frase: ')).upper().split())
    fraseInversa = frase[::-1]
    print(f'\nO inverso de {frase} é {fraseInversa}\n')
    if frase == fraseInversa:
        print('É um palíndromo.')
    else:
        print('Não é um palíndromo.')
else:
    numero = ''
    while not numero.isnumeric():
        numero = str(input('Digite um número: '))
        if not numero.isnumeric():
            print('\nErro. Tente novamente.\n')
    numeroInverso = numero[::-1]
    print(f'\nO inverso de {numero} é {numeroInverso}.\n')
    if numero == numeroInverso:
        print('É uma capicua.')
    else:
        print('Não é uma capicua.')

'''
frase = str(input('Frase: ')).upper()
palavras = frase.split()
fraseJunta = ''.join(palavras)
inversoFraseJunta = fraseJunta[::-1]  # inversoFraseJunta = ''

#for letra in range(len(fraseJunta) - 1, -1, -1):
#    inversoFraseJunta += fraseJunta[letra]

print(f'O inverso de {fraseJunta} é {inversoFraseJunta}.')
if fraseJunta == inversoFraseJunta:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
'''
