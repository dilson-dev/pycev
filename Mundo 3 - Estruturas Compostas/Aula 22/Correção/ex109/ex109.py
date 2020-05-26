# Exercício Python #109 - Formatando Moedas em Python

"""
DESAFIO 109
Modifique as funções que foram criadas no desafio 107/108 para que elas aceitem um
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela
função moeda(), desenvolvida no desafio 108.
"""

import moeda

preço = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preço, 13, True)}')

# Último parâmetro das funções é um valor booleano indicando se deve ou não ter formatação.

# É bom colocar Docstrings (descrições) nas funções ao modularizar.
# Assim facilita bastante na hora de usar a função através do Interactive Help.
# Sendo possível reusar o código em outros projetos, e ajudando o programador, pois está
# utilizando as Docstrings.

# Trabalhar com parâmetro opcional modularizado é simples.
