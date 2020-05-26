# Curso Python #22 - Módulos e Pacotes

# Exemplo de código tradicional usado bastante:
'''
num = int(input('Digite um valor: '))

fat = fatorial(num)
# Não existe a função fatorial implícita no Python, então terá que criar mais para frente.

print(f'O fatorial de {num} é {fat}.')
'''


# Cria-se então o código da função:


def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')


# Vamos criar uma pasta para os módulos para dar um exemplo melhor.

'''
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
'''

# O código ainda está legível, pois está pequeno.
# Adicionamos 2 outras funcionalidades como o dobro e triplo de um número:

'''
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
'''

# O programa ficou um pouco maior, já aumentou o nível da leitura do código, mas imagine
# imagine que ficasse bem grande, que tivesse que calcular várias coisas e fazer uma
# função para cada (funções que sejam úteis no programa).

# Podemos separar o código das funcionalidades do programa principal.
# Criamos o arquivo uteis.py e colocamos todas estas funcionalidades dentro deste.


# Código Fatorial/Funções no Arquivo uteis.py (módulo):
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


# O código principal para calcular o fatorial com apenas 3 linhas:
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')


# Prática

# Até o momento tínhamos um módulo que se chama uteis.py que tinha várias funções
# genéricas:

# uteis.py
# def xyz():
#   ...
# def kxy():
#   ...
# def kkk():
#   ...
# def kmn():
#   ...
# def klk():
#   ...

# import uteis


# O objetivo da modularização é diminuir o código principal e guardar tudo dentro de um
# módulo.

# E se esses módulos ficarem grandes demais? E se dentro do módulo uteis tiver muitas
# funções, muitas mesmo?

# uteis.py
# def xyz():
#   ...
# def kxy():
#   ...
# def kkk():
#   ...
# def kmn():
#   ...
# def klk():
#   ...
# def jhf():
#   ...
# def xuo():
#   ...
# def qwe():
#   ...
# def wrk():
#   ...
# def mmn():
#   ...
# def mnu():
#   ...
# def ouy():
#   ...
# def yuk():
#   ...
# def wpi():
#   ...
# def fpr():
#   ...
# def dsa():
#   ...
# def mbv():
#   ...
# def vxl():
#   ...

# import uteis

# Aí voltam todos os problemas, terá um módulo uteis muito sobrecarregado, com muitas
# funções dificultando a legibilidade e a manutenção, jogando o problema para frente.

# Então a modularização nos ajuda até certo ponto. E aí o que começavámos a fazer dentro
# das linguagens de programação tradicionais era criar vários módulos.

# O Python facilitou muito isso colocando além da criação de outros módulos a junção de
# módulos separados por assunto.

# Que é exatamente o que eles chamam de PACOTE.

# Um Pacote nada mais é do que uma pasta que contém módulos.

# Assim ao invés de ter o uteis.py, teremos um Pacote chamado uteis c/ as mesmas funções
# que tínhamos anteriormente, mas agora podemos separar por assuntos:

# Pacote uteis

# números (tratamento de números)
# def xyz():
#   ...
# def kxy():
#   ...
# def kkk():
#   ...
# def kmn():
#   ...

# strings (tratamento de strings)
# def klk():
#   ...
# def jhf():
#   ...

# datas (compatíveis c/ datas)
# def xuo():
#   ...
# def qwe():
#   ...
# def wrk():
#   ...
# def mmn():
#   ...
# def mnu():
#   ...
# def ouy():
#   ...
# def yuk():
#   ...

# cores (manipulação de cores)
# def wpi():
#   ...
# def fpr():
#   ...
# def dsa():
#   ...
# def mbv():
#   ...
# def vxl():
#   ...


# Agora dentro do nosso Pacote de utilidades agora temos várias funções/módulos separados
# por assunto.
# É exatamente isso que forma um Pacote em Python.

# Para importá-lo é muito simples, basta fazer o mesmo de antes:
# import uteis  # Tudo será importado

# Importação específica de módulos em Pacotes:
# from uteis import datas  # Pega somente a área de datas dentro do Pacote uteis
# from uteis import cores  # Importa só as funções de cores, ou os dois no mesmo projeto

# Para criar este Pacote demonstrado dentro do Python é muito simples, e no PyCharm é
# mais simples ainda, pois como foi dito antes, todo arquivo .py pode ser potencialmente
# um módulo.
# Dentro de um projeto Python toda pasta é considerada um Pacote.

# Assim para criar o Pacote chamado uteis basta criar dentro do projeto uma pasta com o
# nome uteis, e se dentro da pasta chamada uteis quer os módulos números, datas, strings,
# cores, basta criar uma pasta com cada nome destes.
# Assim dentro do Pacote uteis tem outro Pacote, chamado cores, ou até mesmo um módulo
# chamado cores, mas vamos fazer por pastas separadas.

# Assim vamos fazer isso para cada funcionalidade dentro do Pacote uteis:

# Pasta uteis
#   ├────── Pasta cores
#   ├────── Pasta datas
#   ├────── Pasta números
#   └────── Pasta strings

# Temos aqui então toda a organização do Projeto.

# É bom deixar claro que nem sempre iremos utilizar Pacotes nos Projetos.
# Pacotes são para quando seus Projetos ficarem maiores que o 'grande'.
# Quando o Projeto ficar só 'grandinho' módulo dá um jeito.
# Pacotes são para coisas muito maiores.


# Existe uma sintaxe para nomes de arquivos dentro de Pacotes, inclusive um arquivo
# especial que podemos colocar dentro de cada uma das pastas que criamos.
# O nome deste arquivo é __init__.py

# Se tiver utilizando PyCharm nem irá se preocupar com esse nome, pois na hora que criar
# uma pasta/pacote já irá ser criado esse arquivo.

# Assim dentro de cada uma das pastas terá que ter um arquivo __init__, e este arquivo
# não pode se chamar apenas init, tem que ser __init__.py

#  Pasta uteis
#    ├────── Pasta cores
#    |           └───── __init__.py
#    ├────── Pasta datas
#    |           └───── __init__.py
#    ├────── Pasta números
#    |           └───── __init__.py
#    └────── Pasta strings
#                └───── __init__.py


# Inclusive o Pacote principal uteis também pode ter um arquivo init:


#  Pasta uteis
#    |   └───── __init__.py
#    ├─────── Pasta cores
#    |           └───── __init__.py
#    ├───────Pasta datas
#    |           └───── __init__.py
#    ├─────── Pasta números
#    |           └───── __init__.py
#    └─────── Pasta strings
#                └───── __init__.py


# Criamos então a pasta uteis com o arquivo __init__.py dentro desta, que é um arquivo
# vazio.

# Dentro de uteis podemos criar outros pacotes, um pacote pode conter outros pacotes sem
# problema nenhum, ou pode conter simplesmente alguns outros módulos.

# E em uteis teremos outro pacote chamado numeros, cada um c/ seu arquivo __init__.py
# Vamos assim criando os outros pacotes chamados strings, datas, e assim por diante.

# Dentro do arquivo __init__.py do "subpacote" numeros colocamos o código das funções
# que fizemos anteriormente no módulo numeros.

# Para usarmos o pacote de numeros dentro do nosso projeto numeros.py o importamos:

# from <pacote_principal> import <"subpacote">

# from uteis import numeros

# Agora podemos usar todas as funções do arquivo __init__.py do "subpacote" numeros.
