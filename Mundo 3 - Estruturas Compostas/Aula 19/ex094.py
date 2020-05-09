# Exercício Python #094 - Unindo dicionários e listas

"""
DESAFIO 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.

# Alternativas estão diferentes no vídeo da aula e do exercício (anterior é da aula, este é do exercício):
A) Quantas pessoas cadastradas;
B) A média de idade;
C) Uma lista com mulheres;
D) Uma lista com idade acima da média.
"""

pessoas, pessoa = [], dict()
totidade, mulheres = 0, []
repetir = 'S'
while repetir == 'S':
    pessoa['Nome'] = input('\nNome: ').capitalize().strip()

    pessoa['Sexo'] = input('Sexo [M/F]: ').upper().strip()
    while len(pessoa['Sexo']) != 1 or pessoa['Sexo'] not in 'MF':
        print('\nSexo deve ser M ou F. M para Masculino e F para Feminino!')
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper().strip()

    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])

    pessoa['Idade'] = int(input('Idade: '))
    while pessoa['Idade'] < 0 or pessoa['Idade'] > 125:
        print('\nDigite uma idade válida, por favor! (Entre 0 e 125)')
        pessoa['Idade'] = int(input('Idade: '))

    totidade += pessoa['Idade']

    pessoas.append(pessoa.copy())

    print()

    repetir = ''
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('Quer cadastrar outra pessoa? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('\nDigite S para Sim, e N para Não.')

mediaidade = totidade / len(pessoas)

acimamedia = []

for pessoa in pessoas:
    if pessoa['Idade'] > mediaidade:
        acimamedia.append(pessoa)

print('-=' * 35)

print(f'A) Foram cadastradas {len(pessoas)} pessoas no total.')

print(f'B) A média de idade do grupo é de {mediaidade:.2f} anos.')

print(f'C) As mulheres cadastradas foram: {"; ".join(mulher for mulher in mulheres)}.')

print(f'D) Lista das pessoas com idade acima da média: ')

for pessoa in acimamedia:
    print(end='    ')
    for k, v in pessoa.items():
        print(f'{k} = {v};', end=' ')
    print()

print('\n << FIM DO PROGRAMA >>')


# Conforme solução do vídeo:
'''
# Leitura dos dados (adiciona os dicionários com os dados na lista):
galera, pessoa = list(), dict()
soma = média = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)

# Análise dos dados (analisa os dados dos dicionários que estão dentro da lista principal):
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='; ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > média:  # p['idade']  >= média (enunciado pede acima da média)
        print(end='    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n<< ENCERRADO >>')
'''
