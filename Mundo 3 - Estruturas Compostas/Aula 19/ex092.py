# Exercício Python #092 - Cadastro de Trabalhador em Python

"""
DESAFIO 092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

# CTPS = Carteira de trabalho de previdência social
# Pessoa se aposenta depois de 35 anos de contribuição, sem variantes de sexo, por exemplo.

from datetime import date

ano = date.today().year

nome = input('\nNome: ')
nasc = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não tem): '))

idade = ano - nasc

if ctps > 0:
    anocont = int(input('\nAno de contração: '))
    salario = float(input('Salário: R$ '))
    aposentadoria = (anocont + 35) - nasc
    info = {'nome': nome,
            'idade': idade,
            'ctps': ctps,
            'salário': salario,
            'aposentadoria': aposentadoria}
else:
    info = {'nome': nome, 'idade': idade, 'ctps': ctps}

print('\n', '-=' * 35, sep='')
print(f'{info}\n')

for k, v in info.items():
    print(f'{k} = {v}')
