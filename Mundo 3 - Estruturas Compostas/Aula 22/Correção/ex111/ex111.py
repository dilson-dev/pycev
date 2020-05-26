# Exercício Python #111 - Transformando módulos em pacotes

"""
DESAFIO 111
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e
dado.

Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro
pacote e mantenha tudo funcionando.

# Notas
# Foi dado apenas um Ctrl+C, Ctrl+V na pasta/diretório do exercício 110, e renomeado para
exercício 111, assim foi transferido apenas as funções do desafio 110 para o 111;
# No vídeo da solução foi criado dois pacotes e não dois módulos internos.
"""

# 1ª maneira de importar:
from utilidadescev.moeda import resumo

# from utilidadescev import moeda
# import utilidadescev.moeda as moeda

# Os imports acima funcionam tanto no PyCharm quanto Sublime.
# No PyCharm basta marcar o subdiretório como Sources Root para resolver o problema
# do sublinhado vermelho.

# Optei por esta maneira de import, pois funciona tanto no Sublime quanto PyCharm.


# 2ª maneira de importar:
# from ex111.utilidadescev import moeda

# Só funciona no PyCharm ao marcar o diretório principal como Sources Root. E o nome do
# arquivo py deve ser diferente do diretório em que está para não criar conflitos.


# Código principal
preço = float(input('Digite o preço: R$'))
resumo(preço, 35, 22)
