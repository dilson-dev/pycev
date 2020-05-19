# Curso Python #21 - Funções (Parte 2)

# Teoria

# Os 5 Tópicos abordados nesta aula:

# ► Interactive Help (Uma coisa muito importante do Python. Muitas linguagens têm uma documentação muito
# bem organizada, mas nenhuma chega perto do que o Python oferece);
# ► docstrings (documentação do programa). As nossas próprias funções podem ser documentadas;
# ► Argumentos opcionais em funções. Uma característica muito importante do Python, várias outras
# linguagens têm isso também. Mas no Python isso é especialmente útil, importante e valioso;
# ► Escopo de variáveis (Quando uma variável nasce/morre, em que momentos e posições as variáveis são vísiveis.
# Isso também funciona para importação de bibliotecas);
# ► Retorno de resultados (Funções que retornam resultados).


# Interactive Help (Ajuda Interativa). Java/PHP e várias outras lingugens têm uma documentação muito evoluída,
# a comunidade colabora bastante. Há uma série de sites com códigos prontos e manuais de cada um dos comandos.
# O Python também tem isso, mas o Python tem Ajuda Interativa.
# Para obter ajuda interativa no Python é muito simples e fácil, basta usar o comando (função interna) help().
# (Ao abrir e fechar parênteses depois de um nome/identificador isso é uma função/método).

# No console do Python no PyCharm, ou no terminal após digitar python e dar enter, digite help() e dê enter.
# É possível ver a mudança no prompt, que dê três sinais de maiores vai para help>.
# Agora pode digitar qualquer comando, função interna, biblioteca do Python e tem um manual completo.
# A função mais simples, o print, tem um manual, explicando este e cada parâmetro que possui.
# A função len que retorna o tamanho de um objeto, quantos elementos este tem, também tem.
# input que faz a leitura. Há algumas informações que é possível informar.
# datetime mostra tudo (todas as funcionalidades) que esta biblioteca possui, por exemplo.
# Para voltar ao console do Python basta digitar quit, e para finalizar o processo do console basta
# digitar exit()/quit().

# Outra maneira de fazer isso digitando códigos:
# Suponha que não sabe o que a função print faz, basta digitar help(print) que também irá mostrar a
# ajuda interativa.
# help(print)

# Então há essas duas maneiras de obter a ajuda interativa, através do console Python ou no próprio código
# com o comando help(comando).
# help(help)

# Além do help existe uma outra maneira que o Guanabara particularmente não gosta tanto, que é imprimir o doc
# interno dentro de um comando.
# Por exemplo se quiser saber os parâmetros do comando input:
# print(input.__doc__)

# As informações do doc não são necessariamente a mesma coisa que a do help, a formatação é diferente.
# help(input)

# Então é possível fazer das duas maneiras, embora a forma interativa aparente ser mais simples de entender.


# Docstrings

# Esse assunto de Ajuda Interativa nos leva a conhecer um pouco mais sobre docstrings.
# Uma docstring é basicamente uma string de documentação.
# Ao colocar help(input) é mostrada a docstring/manual do "comando" input.
# E todas as funcionalidades internas do Python têm sua própria docstring.

# Exemplo prático de uma função criada:
# def contador(i, f, p):

# Aí surge a dúvida, o que significa i, f e p?
# Assim terá o código da função delimitado a uma área.
# Onde o i é de início, f de fim e p de passo.
# Para quem criou a funcionalidade (nós), isso está muito óbvio/simples.

# Pode ser feita então uma chamada no programa principal:
# contador(2, 10, 2)  # Começa em 2, vai até 10, pulando de 2 em 2.
# O primeiro parâmetro 2 vai para o i, o 10 vai para o f, e o último, 2, vai para o p.
# Assim, existe uma cópia dos valores dos parâmetros chamado de parâmetro real para os parâmetros
# formais que são os que ficam acima na def, os que ficam embaixo são chamados de parâmetros reais ou
# argumentos.
# E essa transferência é realizada de forma automática durante a linha de chamada (contador(2, 10, 2)).


# Assim, dentro da função vai um código de um contador p/ contar do início até o fim, pulando de
# passo em passo:
'''
def contador(i, f, p):
    c = i
    while c <= f:
        print(c, end='..')
        c += p
    print('FIM!')
'''

# contador(2, 10, 2)

# Ao fazer essa chamada de contador tem que saber que o primeiro 2 é o início, o 10 é o fim e o
# último 2 é o passo. Aí surge a dúvida, onde ver isso se não é uma função que eu criei?
# Se é uma função criada por mim eu sei o que é o i, f e p. E se não fui eu que criei ou se alguém
# tá utilizando minha funcionalidade? E isso é totalmente possível no Python e qualquer linguagem de
# programação.
# Será que se colocar help(contador) será mostrado um manual da função criada?

# Imagine que não enxerga o que tem numa função, ou está usando biblioteca de outras pessoas.
# Algo trivial como from time import sleep é um exemplo disso.

# Você não sabe o que é i, f e p. E aí vai tentar utilizar o Interactive Help:
# help(contador)  # Help on function contador in module __main__: contador(i, f, p)

# O resultado será "o help do contador é: contador(i, f, p)"

# Para ter um retorno do "comando" help(contador) com um manual da função criada basta
# criar as docstrings.

# As docstrings entram exatamente entre a definição do contador com a palavra-chave def, e
# o início do código da função, ou seja, após a definição da fuñção:

# def nome_da_função(parâmetros formais):
# <docstring>
# <código da função>


# Para criar uma docstring é bem simples, basta abrir aspas duplas três vezes logo na linha
# abaixo do "comando" def. Uma vez que abra, pode colocar um manual completo como:
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo.
    """
    # Tudo que está entre essas 3 aspas duplas no início da função é a docstring desta.
    c = i
    while c <= f:
        print(c, end='..')
        c += p
    print('FIM!')


help(contador)

# Agora sempre que for executado o comando help da função é exibido a docstring desta.

# Assim é possível criar uma docstring para todas as funcionalidades, que é um "manual" que
# pode ser exibido durante a ajuda interativa. Assim a qualquer momento, se este "comando"
# for importado, é possível exibir a docstring deste ajudando o programador ou usuário que
# estiver usando esta funcionalidade.
'''


# Parâmetros Opcionais (3º Conteúdo)

# Imaginemos uma funcionalidade que some três números
# somar(3, 2, 5)  # Função somar que soma 3, 2 e 5 e retorna o resultado na tela.
# Isso não tem relação com os múltiplos parâmetros com *.
# É possível usar o asterisco como foi feito na aula anterior.
# Assim, trata-se de parâmetros opcionais.

'''
def somar(a, b, c):
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)  # A soma vale 10.
# 3 copiado para variável a, 2 p/ variável b e 5 p/ variável c.

# Mas o que acontece se for colocado menos parâmetros?
somar(8, 4)  # TypeError: somar() missing 1 required positional argument: 'c'
# 8 copiado p/ variável a, 4 p/ variável b, e aí vai ficar faltando uma lacuna, quem vai
# ficar dentro c, qual será o valor de c?

# Se declarar dessa forma, a variável c ficará sem valor, e essa função/chamada dará problema.

# Explicando melhor, ocorrerá um erro, que diz que falta 1 argumento posicional requerido,
# ou seja, falta o 3° argumento.
'''

# Para resolver isso usamos o conceito de parâmetros opcionais:

'''
def somar(a, b, c=0):
    # Assim será recebido a, b, e se não receber c, este valerá 0.

    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)  # A soma vale 10.

somar(8, 4)  # 12
# 8 vai para o a, 4 p/ b, como o c não foi informado (o terceiro argumento), o c receberá 0.
# Assim irá funcionar, sendo somado 8 + 4 + 0, sendo mostrado que a soma que vale 12.

# O c lá em cima é o chamado parâmetro opcional.
'''


# E nada impede em Python de colocar todos os parâmetros como opcionais:
'''
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal Curso em Vídeo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(3, 2)
somar(3)

# Nesse caso chamadas sem passar nenhum valor como argumento também funcionam
somar()  # A soma vale 0.
# Como não foi informado nem a, nem b e nem c, será utilizado os parâmetros opcionais.
# O valor padrão, que no caso para a, b e c é 0 (zero).

# Se for informado 4 valores ainda dará problema:
# somar(3, 3, 5, 8)  # TypeError: somar() takes from 0 to 3 positional arguments but 4 were given

# Se quiser passar 4, 10, 200, ou mais valores terá que utilizar a técnica da aula anterior,
# de múltiplos parâmetros (desempacotamento/empacotamento).

# Nesse caso a função somar pode ser informado de 0 (nenhum parâmetro) até 3 parâmetros, pois
# todos são opcionais.

# Já foi visto isso com a função print.
# Quando o print é digitado ele vem com um parâmetro opcional que tem o valor padrão \n.
# Este parâmetro diz o que será colocado no fim do print. Esse é o parâmetro end.
# O \n cria uma quebra de linha, por isso o print fica em linhas separadas, porque seu end tem uma
# quebra de linha por padrão.
# E por essa mesma razão alguns exercícios têm este parâmetro vazio, para que não ocorra a
# quebra de linha, e fique tudo na mesma linha sem separar os prints.

# É possível com a ajuda interativa ver todos os outros parâmetros opcionais do print:
help(print)
# Os parâmetros opcionais do print são sep=' ', end='\n', file=sys.stdout, flush=False

# Possui também o parâmetro value, e uma reticências que indica que há vários outros parâmetros.
# Observando a documentação é possível ver que o primeiro parâmetro do print é o *objects.
# E esta reticências na verdade indica que a quantidade é indefinida.
# Este parâmetro do print é especial, e foi aprendido na aula anterior.
# Por isso ao usar o print e dar várias vírgulas não existe nenhuma quebra, pois seu primeiro
# parâmetro pode receber uma quantidade indefinida de valores, e todos os outros são opcionais,
# só sendo chamados caso seja explícito que a mudança será nestes.

# É possível também passar os parâmetros de outras maneiras (como visto na aula anterior):
somar(b=4, c=2)  # A soma vale 6.
# 'a' não foi informado então vale 0.

# Inclusive, fora de ordem:
somar(c=3, a=2)  # A soma vale 5.
# 'b' não foi informado então vale 0.

# Então é possível nomear os parâmetros, ou ainda não passar nenhum parâmetro:
somar()

# Esses são os parâmetros opcionais para o Python.
'''


# Escopo de variáveis/declarações

# Basicamente na programação escopo é o local onde uma variável existe e deixa de existir

'''
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}.')  # No programa principal, n vale 2.
teste()
# Na função teste, n vale 2.
# Na função teste, x vale 8.

# Embora o n tenha sido definido no programa principal ele também funciona na função, ou seja,
# no programa inteiro. Esse é o chamado escopo global.

print(f'No programa principal, x vale {x}')  # NameError: name 'x' is not defined
'''
# Ocorre um erro porque a variável x foi declarada dentro da função teste, e assim existe só dentro
# desta função, e portanto funciona só na função em que foi declarada, diferente da variável n que
# funciona no programa principal e também em teste. Esse é o chamado escopo local.
# n é uma variável global, e x é uma variável local.

'''
def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}.')
'''
# print(f'B fora vale {b}.')  # NameError: name 'b' is not defined
# print(f'C fora vale {c}.')  # NameError: name 'c' is not defined
# B e C só funcionam na função e dariam erro por falta de escopo.

# Só que existe um porém, a linguagem Python funciona um pouco diferente de outras linguagens.
# Se por acaso for declado o a dentro da função teste:

'''
def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')  # A dentro vale 8.
    print(f'B dentro vale {b}.')  # B dentro vale 9.
    print(f'C dentro vale {c}.')  # C dentro vale 2.


a = 5
teste(a)
print(f'A fora vale {a}.')  # A fora vale 5.
'''
# Pode pensar que o a vai trocar o valor do 5, mas não é isso que acontece.
# Como foi feito a definição da variável a novamente na função, será criada uma variável a local.
# Existirão assim duas variáveis A, uma local na função e outra global no programa principal.

# O a que recebe 8 não é o global, é o local.

# Teste

'''
def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}.')  # n1 dentro vale 4.  # Local, funciona somente dentro da função


n1 = 2
funcao()
print(f'n1 fora vale {n1}.')  # n1 fora vale 2.  # Global, funciona na função e no programa principal
'''
# O n1 de dentro não afetou o n1 de fora, pois estes têm valores diferentes.


# Além de escopo de variável, existe também escopo de chamada de biblioteca/função.
# Ao fazer a chamada de algo existe a importação global e a local.


# Para tratar a variável a como global é possível no início da def, ou antes de definir o valor de a
# colocar a seguinte frase "global a".
# O "global a" dentro da função diz ao Python que não é para criar uma variável a local, mas usar
# a variável a global.
# Sem isso o Python acaba criando variáveis com escopo local sempre que são definidos novos valores
# dentro deste, independente destas variáveis existirem no escopo global.
'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')  # A dentro vale 8.
    print(f'B dentro vale {b}.')  # B dentro vale 9.
    print(f'C dentro vale {c}.')  # C dentro vale 2.


a = 5
teste(a)  # chamada do teste passando a como parâmetro real, b em def sendo parâmetro formal.
print(f'A fora vale {a}.')  # A fora vale 8.
'''
# Então só é possível usar a variável global dentro das funções se usar a "palavrinha" mágica,
# comando, palavra reservada global. Exatamente como está especificado acima.


# Retornando Valores (Retorno de valores)

# As funções em Python elas podem não retornar, imprimindo dentro delas, ou retornar um valor.

# E para isso será usado uma outra palavra "mágica"/reservada, chamada return.

# Funcionamento do return:
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)  # A soma vale 10.

# Se mandar somar os valores e imprimir na tela irá funcionar, só que terá uma grande limitação.

somar(2, 2)  # A soma vale 4.

somar(6)  # A soma vale 6.
'''
# E se quiser mostrar "As somas valem 10, 4 e 6."?
# Não daria para fazer dessa maneira.

# Então a forma como está a função não é válida.

# Para torná-la válida e funcionar da maneira que se deseja com várias somas com resultados
# diferentes, é possível utilizar o "comando" return no lugar do print:

'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
'''

# somar(3, 2, 5)
# retorna 10. O valor não é exibido porque return não faz nada além de retornar o valor p/ função.

# Será somado então a, b e c em s, dando 10. E será retornado esse s, o 10 pro que vier antes da
# função soma, assim é preciso colocar alguma coisa antes. Esse s vai voltar para a função somar,
# então é necessário colocar algo antes, por exemplo, uma variável resposta:
# resp = somar(3, 2, 5)  # resp = 10

# A variável resposta receberá o resultado de somar
# Assim o valor de s, 3+2+5, que é 10 irá para dentro de resposta, e passará a valer 10.

# Assim como é possível jogar a função com retorno em uma variável também é possível jogá-la em um
# print, exibindo assim o valor do retorno, que sem o print seria simplesmente "perdido".

# print(somar(3, 2, 5))  # 10

# Agora é possível escrever na tela o resultado da soma entre 3, 2 e 5 com a formatação que quiser.
# Dessa maneira é possível ter 3 variáveis com resultados de somas diferentes e exibir esses
# resultados usando o print com a formatação que desejar com resultado das funções.
'''
r1 = somar(3, 2, 5)  # 10
r2 = somar(1, 7)  # 8
r3 = somar(4)  # 4

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
'''
# Assim, funções que retornam resultados são muito úteis quando deseja ter personalização dos
# resultados. Ou seja, quer apenas que a função mande o resultado sem escrever nada além disso.

'''
r1 = somar(3, 2, 5)  # 10
r2 = somar(2, 2)  # 4
r3 = somar(6)  # 6

print(f'Os resultados foram {r1}, {r2} e {r3}.')
'''
# Assim é possível pegar simplesmente o valor que a função retorna através das variáveis e colocar
# na frase personalizada.
# Funções com retorno são muito úteis para programação, sendo bastante usadas.


#
# Prática (Exercício na prática)

# Exercício clássico
# Cálculo do fatorial de um número com retorno para o programa principal para ser mostrado na tela:
"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


'''
n = int(input('Digite um número: '))

print(f'O fatorial de {n} é igual a {fatorial(n)}.')
'''

# Execução de outra maneira
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}.')  # Os resultados são 120, 24 e 1.
"""

# É importante ressaltar que o return não é só para números, é possível retornar um valor
# lógico (verdadeiro ou falso).


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
# print(par(num))

# É possível ainda fazer:
if par(num):
    print('É par!')
else:
    print('Não é par!')

# Assim é possível passar valores para a função e receber valores inteiros, ler valores literais,
# devolver listas, dicionários, tuplas, etc.
