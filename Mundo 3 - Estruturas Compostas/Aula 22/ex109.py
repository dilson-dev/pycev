# Exercício Python #109 - Formatando Moedas em Python

"""
DESAFIO 109
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função
moeda(), desenvolvida no desafio 108.
"""

from ex109 import moeda

preço = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, False)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preço, 13, True)}')

# Tirar formatação pela chamada do usuário e irá colocar um parâmetro.
