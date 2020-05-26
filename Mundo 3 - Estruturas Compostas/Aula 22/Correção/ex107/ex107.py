# Exercício Python #107 - Exercitando módulos em Python

"""
DESAFIO 107
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

import moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10)}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(preço, 13)}')


# Correção
"""
import moeda

# O uso do from, é uma maneira de referenciar (importar) perigosa porque pode ter módulos
# com funções de mesmo nome, assim haveria um conflito no Python, sendo um grande problema.

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')

# Para importar módulo no mesmo diretório basta fazer import <nome_do_módulo>
# PyCharm mostra um sublinhado vermelho no import, para resolver isso basta clicar com
# o botão direito no diretório/pasta > Mark Directory as > Sources Root.
# Embora resolva o problema do import, as funções acabam ficando com um tom de amarelo
# ainda, como se não existissem p/ o PyCharm.


# Com from <modulo> import <funcs>

'''
from moeda import metade, dobro, aumentar

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${metade(p)}')
print(f'O dobro de R${p} é R${dobro(p)}')
print(f'Aumentando 10%, temos R${aumentar(p, 10)}')
'''
"""
