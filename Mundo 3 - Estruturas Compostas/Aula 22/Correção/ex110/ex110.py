# Exercício Python #110 - Reduzindo ainda mais seu programa

"""
DESAFIO 110
Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
até aqui.
"""

import moeda

preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 20, 12)

# Simplicidade do programa com a modularização podendo ser reutilizado em vários códigos
# e projetos.
# No final a programação fica bastante simplificada, pois essa é a ideia da modularização
# em qualquer linguagem de programação.
# No Python isso é ainda mais aprimorado, pois o Python é uma linguagem mais simples.
