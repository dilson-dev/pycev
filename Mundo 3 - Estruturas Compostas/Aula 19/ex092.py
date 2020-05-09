# Exercício Python #092 - Cadastro de Trabalhador em Python

"""
DESAFIO 092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

# CTPS = Carteira de Trabalho e Previdência Social
# Pessoa se aposenta depois de 35 anos de contribuição, sem variantes como a de sexo, por exemplo.

from datetime import date

info = dict()

info['Nome'] = input('\nNome: ').strip().capitalize()
nasc = int(input('Ano de nascimento: '))
info['Idade'] = date.today().year - nasc
info['CTPS'] = int(input('Carteira de Trabalho (0 ou negativo não tem): '))

if info['CTPS'] > 0:
    info['Contratação'] = int(input('\nAno de Contratação: '))
    info['Salário'] = float(input('Salário: R$'))
    info['Aposentadoria'] = (info['Contratação'] + 35) - nasc

print('\n', '-=' * 30, '\n', sep='')

for k, v in info.items():
    print(f'  - {k} = {v}')


# Conforme solução do vídeo:
'''
from datetime import datetime

dados = dict()

dados['Nome'] = input('\nNome: ').strip().capitalize()

nasc = int(input('Ano de nascimento: '))

dados['Idade'] = datetime.now().year - nasc  # datetime.today().year também funciona
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

# Sempre divida o programa em etapas, não tente fazer tudo de uma vez. Teste um pedaço e veja se está ok.

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('\nAno de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

print('-=' * 30)

for k, v in dados.items():
    print(f'  - {k} = {v}')
'''
