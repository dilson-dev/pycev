# Exercício Python #115 - Site está acessível?

"""
DESAFIO 115
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from interface import *
import dados


while True:
    resposta = menu('Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do sistema')

    if resposta == 1:
        titulo('PESSOAS CADASTRADAS')
        dados.exibir('pessoas.txt')
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        dados.registrar('pessoas.txt', nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema... Até logo!')
        break
