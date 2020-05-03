# Curso Python #16 - Tuplas

lanches = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

a = (2, 5, 4)
b = (5, 8, 1, 2)
del a, b[2]
print(a)
print(b)
'''
# c = b + a  # Une uma tupla a outra, e a ordem muda a tupla (diferente da matemática), não sendo a mesma coisa.
print(c.count(111))
print(c)
print(c.index(20))
# começa a contar a partir 0 o índice mostrando a primeira vez que o valor passado no argumento aparece na coleção.
# Se definir um segundo argumento este indicará a posição que deve iniciar a contagem.
# Se o valor não estiver presente na tupla é exibido um erro.
'''
'''
lanche = 'Hambúrguer'
lanche = 'Suco'
'''

# Tuplas são imutáveis

# lanches[1] = 'Refrigerante'  # Não é possível
# lanches = 'H', 'P', 'A', 'Z'  # É possível, mas redefine a tupla inteira

# print(lanches[1:4:2])

# Se não quiser que fique feio pode usar o for

"""
'''É possível escrever os valores da variável composta, tanto com range, como a própria
Apesar de o for escrito com a variável composta propriamente ser mais simples, len é mais diverso.
Algumas situações não é possível resolver somente com a variável composta, sendo preciso usar o len.
'''
'''
# Se não precisar da posição da iteração, maneira mais simples, que escreve menos:
for lanche in lanches:
    print(f'Eu vou lanchar {lanche:12}.')
'''

'''
enumerate pega cada valor dentro de uma coleção e cria uma associação com um número, o primeiro valor 
recebe o número 0, o segundo o número 1, e assim por diante. Por exemplo tupla = ('A', 'B', 'C')
print(list(enumerate(tupla)))
[(0, 'A'), (1, 'B'), (2, 'C')]
'''

'''
Se precisar da posição da iteração, há duas maneiras, a segunda já é bem conhecida, usando range, e 
a primeira usando o enumerate, que além do dado, ele dá a posição, portanto deve colocar no for duas variáveis 
separadas por vírgula.
'''
for ind, elemento in enumerate(lanches):
    print(f'Eu vou lanchar {elemento:12} na posição {ind}.')

# print(lanches)
# print(list(enumerate(lanches)))

'''
for cont in range(len(lanches)):
    print(f'Eu vou lanchar {lanches[cont]:12} na posição {cont}.')
'''
print('\nComi pra caramba!')

''' 
É interessante saber essas 3 maneiras de fazer a mesma coisa, pois cada uma se adapta a um tipo de problema específico.
'''
"""

'''
# Pega os valores da tupla e insere em uma lista em ordem alfabética/numérica. Se a tupla for alfanumérica dará erro.
print(sorted(lanches))
print(lanches)
# Isso não muda a tupla, apenas a mostra de uma maneira organizada, sua característica imutável permanece.
'''