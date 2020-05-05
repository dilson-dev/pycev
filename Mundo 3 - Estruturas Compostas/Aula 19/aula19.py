# Curso Python #19 - Dicionários


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas)  # Mostra o dicionário inteiro


# pessoas[0] dá KeyError, o correto é pessoas['nome']


print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')


print(pessoas.keys())  # Mostra as chaves
print(pessoas.values())  # Mostra valores

# Mostra chaves e valores dentro de uma lista com tuplas. Cada tupla com chave e valor respectivo
print(pessoas.items())


del pessoas['sexo']  # Apaga o elemento (chave e valor)


pessoas['nome'] = 'Leandro'  # Sobrepõe o valor do dicionário


# Adiciona um novo elemento (não é necessário usar o append)
pessoas['peso'] = 98.5


# Acessar chaves e valores e items com laço de repetição:

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

# No caso de dicionários, não é usado o enumerate() de tuplas e listas. É usado o items().


# Dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # uf = unidade federativa
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)

print(brasil)  # [estado1, estado2]

print(brasil[0])  # estado1
print(brasil[1])  # estado2

print(brasil[0]['uf'])  # Rio de Janeiro

print(brasil[1]['sigla'])  # SP


# Problema:
estado = dict()
brasil = list()

# for _ in range(3):
#     estado['uf'] = input('\nUnidade Federativa: ')
#     estado['sigla'] = input('Sigla do Estado: ')
#     brasil.append(estado)

# É criada uma relação, e o último estado adicionado acaba sobrepondo todos os outros, se repetindo na lista.

# brasil.append(estado[:]) dá TypeError: unhashable type: 'slice'

# C/ listas era usado fatiamento [:] que pegava uma cópia dos valores, mas isso ñ funciona e dá erro c/ dicionários.


# Para fazer uma cópia de um elemento sem usar fatiamento, no caso dos Dicionários há um método interno, o copy():
for _ in range(3):
    estado['uf'] = input('\nUnidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

print(brasil)


# Iprime cada dicionário que foi adicionado à variável brasil
for e in brasil:
    print(e)

# Imprime as chaves e valores dos dicionários na lista de forma um pouco mais organizada, em linhas separadas.
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')


# Imprime apenas os valores dos dicionários dentro da lista brasil, na mesma linha.
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

    # Anotação trivial
    # for uf, estado in e.values():  # uf, estado unpack in coleção
    #     print(f'{uf} = {estado}')


# Maneira alternativa que encontrei para fazer o mesmo que antes:
for e in brasil:
    print(f'{e["uf"]} = {e["sigla"]}')
