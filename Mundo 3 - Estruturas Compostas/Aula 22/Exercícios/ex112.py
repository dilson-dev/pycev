# Exercício Python #112 - Entrada de dados monetários

"""
DESAFIO 112
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valore monetários.
"""

from ex112.utilidadescev import dado, moeda

preço = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preço, 35, 22)
