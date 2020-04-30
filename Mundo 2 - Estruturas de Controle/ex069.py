# Exercício Python #069 - Análise de dados do grupo
"""
DESAFIO 069
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final mostre:

A) Quantas pessoas têm mais de 18 anos;  # 18 anos ou mais
B) Quantos homens foram cadastrados;
C) Quantas mulheres têm menos de 20 anos.
"""

sexos = ['M', 'MASCULINO', 'HOMEM', 'MENINO', 'F', 'FEMININO', 'MULHER', 'MENINA']

tot18 = totHomens = totM20 = 0

print()

while True:
    print('–' * 30)
    print(f'|{"CADASTRE UMA PESSOA":^28}|')
    print('–' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = res = ''
    while sexo not in sexos:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo not in sexos:
            print('Erro, dado inválido. Tente novamente.')
    if sexos.index(sexo) <= 3:
        totHomens += 1
    elif idade < 20:
        totM20 += 1

    print('–' * 30)

    while res not in 'SN':
        res = input('Quer continuar [S/N]: ').upper()[0]
        if res not in 'SN':
            print('Erro, tente novamente.')

    if res == 'N':
        break

print(f'\n\n{" FIM DO PROGRAMA ":=^28}')

print(f'\nMaiores de 18 anos: {tot18};\nHomens: {totHomens};\nMoças menores de 20 anos: {totM20}.')
