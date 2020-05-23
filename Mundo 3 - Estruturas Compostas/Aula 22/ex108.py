# Exercício Python #108 - Formatando Moedas em Python

"""
DESAFIO 108

Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado.
"""

from ex108 import moeda as mo

preço = float(input('Digite o preço: R$'))

print(f'A metade de {mo.moeda(preço)} é {mo.moeda(mo.metade(preço))}')
print(f'O dobro de {mo.moeda(preço)} é {mo.moeda(mo.dobro(preço))}')
print(f'Aumentando 10%, temos {mo.moeda(mo.aumentar(preço, 10))}')
print(f'Diminuindo 13%, temos {mo.moeda(mo.diminuir(preço, 13))}')

# Reaproveitamento de código através da modularização.
# Reaproveitar código do exercício 107 para o 108 sem alterar o 107, deixando preservado
# o que foi feito no 107.


# Código conforme vídeo da aula:
'''
from ex108 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {mo.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {mo.moeda(moeda.diminuir(p, 13))}')
'''
