# Exercício Python #002 - Respondendo ao Usuário

"""
DESAFIO 002
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""

nome = input('Qual é o seu nome?\033[1;30m ')
print('\nSeja bem vindo(a) {}{}{}! É um prazer te conhecer!'.format('\033[34m', nome, '\033[1;30m'))
