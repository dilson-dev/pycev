# Exercício Python #108 - Formatando Moedas em Python

"""
DESAFIO 108

Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado.
"""

import moeda  # as mo

preço = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(preço, 13))}')


# Reaproveitamento de código através da modularização c/ Ctrl+C, Ctrl+V na pasta/pacote
# que tem os módulos.

# <módulo>.<função>
#    moeda.moeda()


# Código conforme vídeo da aula:
'''
from ex108 import moeda
# Import dessa forma para retirar o sublinhado vermelho de erro do PyCharm.
# No meu caso isso não funcionou, deu erro.
# Para resolver e não sublinhar em import <módulo> basta clicar com botão direito na
# pasta e definir como source root. O diretório ficará azul e o sublinhado sumirá.

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {mo.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {mo.moeda(moeda.diminuir(p, 13))}')
'''


# Outra maneira de formatar moedas com locale

'''
import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
locale.setlocale(locale.LC_ALL, 'pt')

# R$ fica com um espaço: R$ <valor> e tem pontos a cada 3 uniaddes por exemplo 1.000
print(f'Valor: {locale.currency(preço, grouping=True, symbol="R$")}')

# Se quiser o R$ junto: R$<valor> e sem os pontos:
print(f'Valor: R${locale.currency(preço, symbol=None)}')
'''
