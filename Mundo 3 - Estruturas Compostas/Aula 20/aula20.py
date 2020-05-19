# Curso Python #20 - Funções (Parte 1)

"""
# Teoria

'''
def lin():
    print('-' * 30)


# Entre o def e o programa principal deve haver 2 linhas vazias, é uma questão estética, de organização do código

# Ao executar o programa as defs não são executadas.
# As funções só serão executadas ao ser chamado o cabeçalho (nome da função com os parênteses).

# Assim, todas as vezes que for necessário escrever uma linha é só colocar  no código, que isso será
# executado:

# Caso o def seja retirado do código, ocorrerá um erro, pois não existirá mais o determinado "comando".

# O def cria um "comando" novo, o lin nesse caso, que ao ser chamado cria uma linha.

# Programa Principal
lin()
print(f'| {"CURSO EM VÍDEO":^26} |')
lin()
print(f'| {"APRENDA PYTHON":^26} |')
lin()
print(f'| {"GUSTAVO GUANABARA":^26} |')
lin()
'''

# É possível usar parâmetros e resumir ainda mais o código anterior, pois há um padrão a cada 3 linhas.
# txt então é recebido como parâmetro, e o texto que quer exibir é passado como argumento na chamada da
# função.


# No Pycharm há setinhas que podem ser usadas para contrair a função ficando uma reticências (...) no lugar.


def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
título(f'| {"CURSO EM VÍDEO":^26} |')

# título(f'| {"APRENDA PYTHON":^26} |')

# título(f'| {"GUSTAVO GUANABARA":^26} |')

# A função título pode ser executada com qualquer outra string:
título('     PYTHON É MUITO BOM!     ')

# A função título agora mostra sempre uma linha em cima, uma embaixo e a mensagem no meio.
# Mensagem que for colocada entre os parênteses.

# Podem ser colocadas mensagens pequenas também como 'Oi':
título('Oi')

# E a linha sempre terá o mesmo tamanho de 30 caracteres que foram definidos na função.
# Mas é possível fazer com que as linhas se adaptem ao tamanho da frase.

# O programa principal tem apenas 3 linhas de código que são executadas, nesse caso os "comandos" título.

# Só que a palavra título não é um comando que vem no Python de fábrica, foi possível definir esta com def:
# def nome_da_função():
#   <bloco de código>

# Assim foi possível tornar título um "comando" reconhecido para este programa em específico, onde def está.

# Existe além disso a modularização no Python, sendo possível jogar esse "comando" em outro lugar.

# Em suma, título é tido como uma rotina, algo que acontece constantemente nos programas.
# Coisas que acontecem constantemente, o ideal é criar uma função, exatamente como foi feito aqui.

# Funções sem parâmetro x Funções com parâmetro
"""

# Prática

# Uma dúvida muito comum entre alunos em sala de aula é:
# P: Mas para que eu preciso de uma função se eu posso simplesmente colocar o código no programa?
# R: É muito difícil visualizar a utilidade de funções em uma aula porque os programas são sempre pequenos.
# As funções só passam a ser úteis quando os códigos ficarem muito grandes e repetitivos.
# Por exemplo quando a mulher chega pro homem e diz que o relacionamento virou uma rotina, e deve dar um
# jeito para resolver, é a mesma coisa.
# Assim também é com a programação, quando seu programa começar a ter coisas repetitivas, quando se tornar
# uma rotina, deve resolver também, para não se tornar algo cansativo e você ter que ficar escrevendo
# código várias vezes, ou copiando e colando. Aí é só escrever uma vez, e tudo fica resolvido.

# Exemplos utilizando funcionalidades
"""
'''
a = 4
b = 5
s = a + b
print(s)
'''
# No lugar dessas linhas repetitivas seria ótimo ter um programa que somasse os valores
soma(4, 5)

'''
a = 8
b = 9
s = a + b
print(s)
'''
soma(8, 9)

'''
a = 2
b = 1
s = a + b
print(s)
'''
soma(2, 1)

# Não é uma necessidade comum a todos os programadores, mas é para nós, precisamos muito dessa solução.
"""

# Programa Principal
'''
soma(4, 5)
soma(8, 9)
soma(2, 1)
'''
# Obviamente ao executar dará erro, porque não existe em Python o "comando" soma.
# Mas é possível criar, personalizar, definir soma. Já que o Python não sabe o que é soma, definimos:

'''
def soma(a, b):
    s = a + b
    print(s)


# Programa Principal:
soma(4, 5)
soma(8, 9)
soma(2, 1)

# 4, 5 e 8, 9 e 2, 1 são os parâmetros/argumentos passados à função.

# soma(4)  # TypeError: soma() missing 1 required positional argument: 'b'
# Erro, porque a soma recebe 2 parâmetros, e foi passado apenas 1.

# Para resolver isso deve passar mais um parâmetro.
soma(4, 1)

# Dessa forma é necessário colocar os 2 parâmetros definidos na função soma.

# É possível também explicitar os parâmetros passado a função:
soma(a=4, b=5)

# É possível também inverter, colocando b=4 e a=5, sem problema algum:
soma(b=4, a=5)
# Assim, é possível mudar a ordem, contato que explicite os parâmetros passados à função.
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma A + B = {s}.')


# Programa Principal
soma(4, 5)

# Mesmo resultado da linha anterior:
soma(a=4, b=5)

# Mas é possível trocar/mudar a ordem sem problemas:
soma(b=4, a=5)

# Se tentar fazer alternado entre igualdade e sem igualdade ocorre um erro, pois não há essa inteligência
# na linguagem de saber a quantidade de argumentos, e ter noção de que o B é 4, e então o A seria 5.

# soma(b=4, 5)  # SyntaxError: positional argument follows keyword argument

# Assim se for explicitar os parâmetros passados, precisa explicitar todos os dois: soma(b=4, a=5)

# Se não explicitar, o primeiro valor passado vai para A, e o segundo valor vai para B:
soma(7, 2)
# Existe uma cópia desse valor

# Em soma(b=4, a=5) o 4 é passado para o B em def soma(a, b), e o 5 é passado da mesma maneira para o A, e
# executando o código da função.
# Em soma(7, 2) o 7 é passado para o A em soma(a, b), e o 2 é passado para o B da mesma maneira. Fazendo
# a conta também.

# Se tentar colocar mais parâmetros do que os passados também ocorrerá erros:
soma(3, 9, 5)  # TypeError: soma() takes 2 positional arguments but 3 were given
# O 3 vai para o A, o 9 vai para o B, e o 5 vai para quem? Não há espaço para colocá-lo.
# Se foi colocado na definição que soma recebe 2 valores, soma deve receber 2 valores.
# Se for passado 3, obviamente dará erro.
'''

# Mas, o Python como uma linguagem moderna e que quer lhe ajudar tem o conceito de empacotar parâmetros.

# Imagine que existisse uma funcionalidade chamada contador, e que gostaria de contar quantos números foram
# passados
# contador(5, 7, 3, 1, 4)  # Retornaria que foram passados 5 números
# contador(8, 4, 7)  # Retornaria que foram passados 3 números.

# A maioria das linguagens de programação não permite fazer isso, mas o Python permite.
# Isso é chamado de empacotamento.

# Para fazer isso criamos então a função com o identificador contador, e passamos um parâmetro especial,
# com um asterisco antes deste. O asterisco (*) é o símbolo de desempacotar e define que a quantidade de
# parâmetros que será recebida é indefinida, ou seja, podem ser recebidos a quantidade de parâmetros que
# forem, e estes poderão ser processados na função.
# Os parâmetros são recebidos como uma tupla, independente de ser apenas 1 elemento, é recebido como uma
# coleção do tipo tupla, e assim é possível fazer com este parâmetro tudo que é feito com uma tupla.

"""
def contador(* núms):
    # print(núms)
    '''
    for valor in núms:
        print(valor, end=' ')  # print(f'{valor} ', end='')
    print('FIM!')
    '''
    tam = len(núms)
    # print(f'Recebi os valores {núms} e são ao todo {tam} números.')

    # Prezando pelo visual:
    # print(f'Valores: {" ".join(str(v) for v in núms)};')

    # Melhor ainda:
    print('Valores:', end=' | ')
    [print(f'{n}º = {val}', end=' | ') for n, val in enumerate(núms, 1)]
    print(f'\nQuantidade: {tam}.\n')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
contador(2)
"""


# Outra coisa possível de fazer é trabalhar com listas ao invés de tuplas, já que as tuplas são meio
# limitadas, pois não podem ser alteradas.

# valores = [7, 2, 5, 0, 4]
#            0  1  2  3  4

# A vantagem da lista é que esta é alterável.

# Ao fazer a declaração de valores, é criada uma variável composta e única com seu valores indexados (0, 1, 2, etc).

# Supondo que quisesse que a lista valores fosse dobrada (7 virava 14, 2 virava 4, 5 virava 10, etc).
# Poderia existir um "comando" dobra(), que dobraria os valores dentro da lista.
# Isso não é algo que faz muito sentido, mas suponha que em uma determinada situação precise fazer isso
# com uma certa frequência.

# Nessa situação não é preciso empacotar/desempacotar. Já que a lista já é uma variável composta, é
# possível passá-la como parâmetro diretamente dentro dos parênteses:
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# valores = [7, 2, 5, 0, 4]  # [14, 4, 10, 0, 8]
valores = [6, 3, 9, 1, 0, 2]  # [12, 6, 18, 2, 0, 4]
dobra(valores)
print(valores)
'''
# É criada uma referência do parâmetro que foi passado (valores) no momento da chamada da função dobra.
# Essa referência é passada para a função, e nesse momento existirão duas listas na memória.
# Uma lista chamada valores, e uma lista chamada lst. E tudo que for feito em lst interefere em valores
# diretamente.

# Para quem é mais experiente e aprendeu fundamentos de programação, irá notar que para o Python toda
# passagem de parâmetro é por referência, diferente de outras linguagens como C e Java, onde a passagem
# de parâmetros é por valor.

# Então tudo que for feito em lst irá interferir na lista valores.
# Isso não é um desempacotamento. Desempacotar é aquilo feito anteriormente.
# Um exemplo anterior com a função soma usando empacotamento/desempacotamento:


def soma(* valores):
    # print(sum(valores))
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma}.')


soma(5, 2)
soma(2, 9, 4)

# As linhas acima com o * são um exemplo de desempacotamento, já o que foi feito com listas é uma outra técnica.
# Ambas são válidas em Python, mas em algumas situações é melhor utilizar desempacotamento, e outras, listas.
