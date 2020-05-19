# Exercício Python #031 - Custo da Viagem

"""
DESAFIO 031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longes.
"""

d = int(input('\033[1;30mDigite a distância da viagem em Km: '))
print('\n\033[1;35mCom a distância de {}Km'.format(d), end=' ')
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print('o preço da viagem será de \033[1;32mR${:.2f}\033[m\033[1;34m.\nTenha uma boa viagem!'.format(p))


# Solução conforme o vídeo:
"""
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
print('O preço da sua passagem será de R${:.2f}.'.format(preço))
"""

"""
A condição simplificada do if e else inverte a estrutura, primeiro é colocado o bloco a ser executado, e depois
a condição que o validará caso seja verdadeira, assim fica <bloco> if <condição> else <outro_bloco>.
Não são usados os dois pontos, e apenas expressões são válidas, ou seja, não é possível executar comandos
através dessa estrutura.
"""
