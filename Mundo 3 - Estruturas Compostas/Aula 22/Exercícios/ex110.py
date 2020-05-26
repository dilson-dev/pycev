# Exercício Python #110 - Reduzindo ainda mais seu programa

"""
DESAFIO 110
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
até aqui.
"""

from ex110 import moeda

preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 80, 35)
