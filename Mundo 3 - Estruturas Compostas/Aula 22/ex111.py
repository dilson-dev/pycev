# Exercício Python #111 - Transformando módulos em pacotes

"""
DESAFIO 111
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e
dado.

Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.

# Até o 110 também
"""

from ex111.utilidadescev import moeda

preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 35, 22)
