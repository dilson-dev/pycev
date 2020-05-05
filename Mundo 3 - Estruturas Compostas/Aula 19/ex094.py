#

"""
DESAFIO 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.
"""

pessoas = []
repetir = 'S'
while repetir == 'S':
    nome = input('\nNome: ').capitalize().strip()
    sexo = input('Sexo [M/F]: ').upper().strip()
    while len(sexo) != 1 or sexo not in 'MF':
        print('\nSexo deve ser M ou F. M para Masculino e F para Feminino!')
        sexo = input('Sexo [M/F]: ').upper().strip()
    idade = int(input('Idade: '))
    while idade < 0 or idade > 125:
        print('\nDigite uma idade válida, por favor! (Entre 0 e 125)')
        idade = int(input('Idade: '))

    pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})

    repetir = ''
    while len(repetir) != 1 or repetir not in 'SN':
        repetir = input('\nQuer cadastrar outra pessoa? [S/N] ').upper().strip()
        if len(repetir) != 1 or repetir not in 'SN':
            print('Digite S para Sim, e N para Não.')

print('\n', '-=' * 35, '\n', sep='')

print(f'- Foram cadastradas {len(pessoas)} pessoas no total.')

totidade = 0
mulheres = []
for pessoa in pessoas:
    totidade += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

mediaidade = totidade / len(pessoas)

print(f'- A média de idade do grupo é de {mediaidade:.2f} anos.')
print(f'- As mulheres cadastradas foram: {" ".join(mulher for mulher in mulheres)}.')

acimamedia = []
print('\n\n- Lista de pessoas com idade acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > mediaidade:
        print()
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()

print('\n\n << FIM DO PROGRAMA >>')
