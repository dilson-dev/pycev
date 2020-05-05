# Exercício Python #029 - Radar eletrônico

"""
DESAFIO 029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input('Digite a velocidade do carro: '))
# print('O limite de velocidade é de 80Km/h.')
# multa = (velocidade - 80) * 7
# print(('Você foi multado, a sua multa é de R${:.2f}'.format(multa) if velocidade > 80 else ''))
if velocidade > 80:
    print('\nVocê foi multado! ')
    multa = (velocidade - 80) * 7
    print('A sua multa é de R${:.2f}.'.format(multa))
"""
else:
    print('\nVocê está dentro do limite de velocidade, não será multado.')
"""
print('Se for dirigir, não beba!')  # Mas se for beber me chame!


# Programa feito no vídeo:
'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {}R${:.2f}!'.format('\033[33m', multa))
print('\033[32mTenha um bom dia e dirija com segurança!')
'''

"""
Essa estrutura que não utiliza o else só o if é chamada de condição simples.
Existe também a condição composta que usa os dois, else e if e a condição simplificada que é feita somente em uma linha
com o print, simplificada como o nome sugere.
"""
