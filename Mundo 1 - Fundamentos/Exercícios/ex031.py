# Exercício Python #031 - Custo da Viagem
d = int(input('\033[1;30mDigite a distância da viagem em Km: '))
print('\n\033[1;35mCom a distância de {}Km'.format(d), end=' ')
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print(
    'o preço da viagem será de \033[1;32mR${:.2f}\033[m\033[1;34m.\nTenha uma boa viagem!'.format(p))


distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
print('O preço da sua passagem será de R${:.2f}.'.format(preço))

"""
Lógica da condição simplificada(If simplificado) você utiliza o que está dentro da identação primeiro, aí usa a primeira
do if se ele fosse utilizado normalmente e após isso usa-se o else normal, porém sem os pontos, tudo na mesma linha.
"""
