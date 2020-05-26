# Exercício Python #112 - Entrada de dados monetários

"""
DESAFIO 112
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores monetários.
"""

# from ex112.utilidadescev import moeda, dado
from utilidadescev import moeda, dado

preço = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preço, 35, 22)

# Na hora de utilizar facilita bastante com a sintaxe menor e mais simples.
# Preço é um dado do tipo dinheiro e tem a mensagem ali.
