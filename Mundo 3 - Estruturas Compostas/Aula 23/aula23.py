# Curso Python #23 - Tratamento de Erros e Exceções

# É um assunto muito importante para toda linguagem de programação.
# A maioria das linguagens de programação, principalmente as mais modernas têm tratamento
# de erro e exceções. E não poderia ser diferente com o Python, já que é uma linguagem
# mega moderna.

# Erros acontecem nos programas também, softwares não são imunes às falhas.
# Falhas irão acontecer no Python e devemos estar preparados para lidar com essas falhas,
# tratando-as.

# Esses erros que acontecem nos programas às vezes não são planejados e isso acontece
# sempre, toda hora há uma falha que não estava planejando nos programas.

# Aprenderemos como tratar e tentar solucionar a maioria dos erros que acontecem em
# nossos programas.

# E ao falar de erros não está se tratando de erros como: primt(x)

# Foi trocado a letra n pela letra m, sendo um erro de sintaxe.

# É como se falasse 'poblema'.

# Foi errado sintaticamente, foi trocado as letras.

# O Python e nenhuma linguagem de programação irá aceitar essa troca de letras.

# Não é esse tipo de erro a que está se referindo.

# Está se referindo a outro tipo de erro: print(x)

# Podes concluir que agora o programa está funcionando, pois não há erros sintáticos.
# E esse é um erro muito comum de quem está começando.

# Muitos dizem ao Guanabara que o programa que escreveram deu erro, mas está certo.

# Estar certo e estar livre de erros tem uma diferença muito grande.

# Muitos iniciantes acham que se trocar a letra n do print pelo m está tudo bem, mas
# não está, ou se esquecer os parênteses do print, também não está tudo bem.
# Isso porque o compilador dá erros de sintaxe, erros sintáticos no programa.
# E erro sintático é só um tipo de erro, um erro fundamental, mas não é o único.

# O exemplo do comando do print pode não ter erro sintático nenhum, mas pode dar problema.

# Comandos sem erros sintáticos não estão livres de terem outros tipos de erros.
# Erro de sintaxe, sintático, não é o único tipo de erro que pode ocorrer.


# Teoria

# print('Oi')  # Programa funcional, processo é finalizado normal com exit code 0.

# print(x)  # Tá com um problema.

# Apesar de não ter erros sintáticos, a variável x não foi inicializada.
# Assim:

# x = 8
# print(x)


# Assim o print(x) sem declarar a variável não é um erro sintático.

# É um erro de significado, semântico.

# Embora digite o comando certinho, isso pode acarretar em um erro:

# print(x)

# Erro que aparece no terminal:
'''
Traceback (most recent call last):
File ".\aula23.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
'''
# Foi dito que na linha 1 teve um problema e que esse erro se chama NameError, ou seja,
# um erro de nome. Então mesmo que o comando esteja "correto", digitado corretamente,
# há um erro.

# Assim o comando print(x) tem uma falha, porque a variável x simplesmente não existe.

# E quando esse erro não se dá de forma sintática, ou seja, seria um comando que
# normalmente funcionaria, não damos a isso o nome de erro, mas de exceção.
# Nesse caso foi disparada uma exceção chamada NameError.

# Outra exceção muito comum:
# n = int(input('Número: '))

# Tá tudo digitado correto, tecnicamente não há erros.

# Colocando 7 como a entrada funciona normalmente:
# Número: 7 -> Process finished with exit code 0

# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

# O número 8 também funciona sem problemas:
# Número: 8 -> Você digitou o número 8 -> Process finished with exit code 0

# O comando está tecnicamente certo/correto, tanto é que funcionou.

# Só que existem algumas exceções.

# Por exemplo, escrever o número por extenso como 'oito', 8 é um número só que o Python
# não interpreta números por extenso como números, mas como strings.
# Sendo assim:
# Número: oito -> Process finished with exit code 1
# Erro:
'''
Traceback (most recent call last):
  File ".\aula23.py", line 1, in <module>
    n = int(input('Número: '))
ValueError: invalid literal for int() with base 10: 'oito
'''
# Erro na linha 1, mas não há erro na linha 1, mas não foi um erro, foi uma exceção.
# Foi uma exceção chamada ValueError. É um erro de valor, pois estava esperando um valor
# do tipo inteiro, e acabou recebendo um valor do tipo string.

# Sendo assim deu um erro na hora de atribuição de n, pois foi digitado o valor errado,
# foi digitado a palavra 'oito', e essa palavra não pode ser convertida para inteiro
# pela função int.
# Isso também disparou para nós uma exceção, o ValueError.

# Outro exemplo de comando válido:
# r = a / b

# Sem problema, o comando está certo.

# Exemplo de programinha para mostrar que está tudo funcionando corretamente:

# a = int(input('Numerador: '))  # Valor de cima de uma divisão
# b = int(input('Denominador: '))  # Valor debaixo de uma divisão
# r = a / b
# print(f'O resultado é {r}')

# Não há erro sintático nenhum. A variável foi declarada, está tudo certo.

# Ao colocar os valores inteiros 5 e 2 é retornado o resultado 2.5, um valor real
# sem problemas.

# Input
# Numerador: 5
# Denominador: 2

# Output
# O resultado é 2.5

# Process finished with exit code 0

# Se for digitado uma palavra acontecerá um exceção ValueError como vimos anteriormente.

# Mas existe outra exceção que pode ocorrer aqui:

# Input
# Numerador: 8
# Denominador: 0

# Na matemática a divisão por 0 é um problema. Esta divisão não existe no campo dos
# números inteiros e reais.

# Output
'''
Traceback (most recent call last):
  File ".\aula23.py", line 3, in <module>
    r = a / b
ZeroDivisionError: division by zero
'''

# Ocorreu outra exceção.

# Diferença entre erro e exceção, falha sintática e uma exceção.

# Ocorreu outra exceção, chamada ZeroDivisonError.

# Que é um erro de divisão por zero, pois divisão por zero não pode ocorrer.

# E na linha 3 foi tentando fazer uma divisão por zero, pois b era zero.

# Sendo assim se tem o denominador, no caso o b em r = a / b, igual a zero, o valor
# numérico 0 há um exceção disparada o ZeroDivisionError

# Outros exemplos:

# r = 2 / '2'

# Dois dividido por dois é 1, mas o segundo dois é um número?
# Algumas linguagens de programação até considerariam um número, como por exemplo
# JavaScript e PHP. Só que o Python não.
# Para o Python dois dividido por dois escrito exatamente dessa maneira com o último dois
# entre aspas ou até o primeiro dois entre aspas é uma exceção chamada TypeError ou Erro
# de Tipo.

# Outro exemplo muito clássico, uma falha muito clássica ao programar usando listas:

# Exemplo:
# lst = [3, 6, 4]
# print(lst[3])

# Pode responder sem pensar que o terceiro valor na lista é 4, porém se esqueceu que
# o índice em listas começa a partir do 0, portanto o índice 3 se refere ao quarto valor,
# que não existe na lista. Assim é gerada uma exceção chamada IndexError.

# A maioria das linguagens de programação, e isso inclui o Python, considera o primeiro
# índice de tudo, o índice 0.

# E esse tipo de falha, exceção é conhecida como IndexError.
# No casos dos dicionários isso é chamado de KeyError, que na verdade o índice é chamado
# de key, chave.

# Exemplo:
# import uteis

# Criado o módulo uteis e importado, tá tudo certo, mas e esse módulo não existir?
# E se tentou importar uteis e este não existe?
# Basta que este arquivo, o uteis.py não seja encontrado para que se dispare uma exceção
# também, e essa exceção se chama ModuleNotFoundError, que é o erro de módulo não
# encontrado.


# O Python é repleto de exceções, algumas delas:

# NameError
# ValueError
# ZeroDivisonError
# TypeError
# IndexError
# KeyError
# EOFError
# KeyboardInterrupt
# OSError
# MemoryError
# ConnectionError
# RuntimeError

# Não tem como decorar todas as exceções, uma dica é ir no Google e digitar Python Exceptions,
# ou Python Exception List, que é a lista de exceções de Python.

# Irá ver a real quantidade de exceções, se está achando que as que foram mostradas é muito
# está redondamente enganado.

# Não precisa se desesperar, algumas pessoas pensam em decorar/aprender tudo isso, mas não é
# necessário. Aos poucos, naturalmente elas irão ocorrer e é possível identificar o nome das
# exceções nos erros do código.

# Toda exceção no caso do Python é filho de uma classe maior chamada Exception, assim como
# está escrita, com 'e' maiúsculo.
# Assim sempre que ver essa palavra Exception irá ler como 'exceção'.
# Exceções são um tipo de erro que não ocorre sempre.
# Basicamente foi digitado corretamente sem erros sintáticos, mas está acontencedo um erro.
# Isso é chamado de exceção.

# Podemos 'lidar com / tratar' exceções.

# Para tratar uma exceção com Python usamos um comando.

# Até o momento temos o uso da linguagem bastante imperativo, 'mandando' esta fazer as coisas.
# 'print alguma coisa', 'input alguma coisa'

# Ao invés de 'mandarmos' podemos 'tentar' fazer alguma coisa.
# Então começa o comando try dentro da linguagem. Várias linguagens de programação tem a
# estrutura try, que quer dizer 'tente'. PHP, Java e o Python também tem.

# Assim vamos usar a estrutura try except, que é 'tente' alguma coisa, senão acontece uma
# exceção.

# Assim será colocado o try, dois pontos, identado, e dentro do bloco do try irá o que
# geralmente pode dar problema, o(s) comando(s) que normalmente daria(m) problemas.

# E na parte debaixo no except irá colocar uma outra área, que é a área da falha.
# Isso é se tentar uma coisa em cima, e falhar, o que é que vai acontecer?

# Essa é a estrutura básica do comando:

# try:
#    <operação>
# except:
#    <falhou>


# Programa de ler os dois números e dividir um pelo outro sem receber mensagem de erro.

# Prática

# a = int(input('Numerador: '))  # 8
# b = int(input('Denominador: '))  # 0
# r = a / b
# print(f'O resultado é {r}')

# Output: ZeroDivisionError

# Ao invés de 'mandar' fazer tudo isso... Vamos fazer o seguinte:

# try:  # tente fazer os comandos
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:
#     print('Infelizmente tivemos um problema :(')

# print(f'O resultado é {r}')

# Teste 1

# Numerador: 5
# Denominador: 2
# O resultado é 2.5

# Process finished with exit code 0

# Funcionou o resultado é 2.5, sem problemas.


# Teste 2

# Numerador: oi
# Infelizmente tivemos um problema :(
# Traceback (most recent call last):
#   File ".\aula23.py", line 8, in <module>
#     print(f'O resultado é {r}')
# NameError: name 'r' is not defined

# Ocorreu um NameError porque tentou imprimir o r na tela.
# Só irá fazer com que o r seja dividido, criado se não der erro na atribuição do a e do b.

# Para isso também tem uma parte do comando.

# Temos então:

# try:  # Para tentar
#     <operação>
# except:  # Se der problema
#     <falhou>

# E se não der problema? Aí usamos o else:

# try:
#     <operação>
# except:
#     <falhou>
# else:
#     <deu certo>

# Dentro da área do else irá dizer o que irá acontecer se deu certo, se o try deu certo.

# try:  # Irá tentar fazer
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:  # Se der problema
#     print('Infelizmente tivemos um problema :(')
# else:  # Se não
#     print(f'O resultado é {r:.1f}')

# Testes

# Numerador: 5
# Denominador: 3
# O resultado é 1.7

# Se por acaso der problema agora

# Tentativa 2
# Numerador: 5
# Denominador: 0
# Infelizmente tivemos um problema :(

# Já não tem mais mensagem de erro. Isso é tratamento de erro.

# Existe ainda uma outra cláusula que podemos colocar abaixo do else.
# Essa última cláusula é o finally, que quer dizer 'finalmente'.
# Esse vai acontecer independente se deu certo ou se deu erro.
# É importante dizer que as cláusulas else e finally são opcionais, nem sempre é necessário
# usá-las.

# try:  # Irá tentar fazer
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except:  # Se der problema
#     print('Infelizmente tivemos um problema :(')
# else:  # Se não
#     print(f'O resultado é {r:.1f}')
# finally:  # Irá acontecer sempre.
#     print('Volte sempre! Muito obrigado!')

# Por exemplo, o finally pode ser usado para fechar um banco de dados, um arquivo aberto,
# dando certo ou dando errado tem que fechar o banco, tem que fehcar o arquivo.


# Testes

# Numerador: 10
# Denominador: 5
# O resultado é 2.0
# Volte sempre! Muito obrigado.

# Numerador: 45
# Denominador: nove
# Infelizmente tivemos um problema :(
# Volte sempre! Muito obrigado!

# Inclusive é possível tratar esse erro, mostrar o que aconteceu.

# É possível colocar do lado do except aquela palavrinha, que é aquela classe principal,
# que é o Exception, com 'e' maiúsculo.

# (...)
# except Exception as erro:
#    print('Infelizmente tivemos um problema :(')
# (...)

# Agora temos uma variável que é possível mostrar a formatação, ao invés de escrever
# 'Infelizmente tivemos um problema' que é uma coisa genérica podemos escrever:

# Ao escrever 'erro.' podemos ver que tem:
# __cause__ = Causa
# __class__ = Classe
# __context__ = Contexto

# Vamos então colocar a classe:

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')


# Testes

# Numerador: 10
# Denominador: 2
# O resultado é 5.0
# Volte sempre! Muito obrigado!

# Sem problemas, tudo funcionando

# Agora se for:

# Numerador: 5
# Denominador: oi
# O problema encontrado foi <class 'ValueError'>
# Volte sempre! Muito obrigado!

# Foi encontrado um erro de valor, assim, já foi dito qual é o tipo de exceção.

# Numerador: 7
# Denominador: 0
# O problema encontrado foi <class 'ZeroDivisionError'>
# Volte sempre! Muito obrigado!

# Foi encontrado um erro de divisão por zero.

# É claro que não irá mostrar isso para o usuário, mas enquanto estiver desenvolvendo.
# O desenvolvedor irá poder capturar qual é o erro e mostrar na tela uma mensagem personalizada

# E essa mensagem personalizada é possível porque a estrutura do try pode se expandir muito,
# na verdade todo try pode ter mais de um except.
# O except de cima tem que ter qual é o tipo de erro, o código da exceção, a classe da exceção.
# Assim pode ter vários excepts para outros tipos de exceção e cada um deles terá seu próprio
# bloco, mensagem e tratamento.

# Assim um mesmo try pode ter vários excepts:

# try:
#     <operação>
# except TypeError:
#     <falhou>
# except ValueError:
#     <falhou>
# except OSError:
#     <falhou>
# else:
#     <deu certo>
# finally:
#     <certo/falha>


# Assim podemos pegar o except anterior e ao invés de Exception e o except genérico de
# 'tivemos um problema':

# (...)
# except Exception as erro:
#     print(f'O problema encontrado foi {erro.__class__}')
# (...)

# Podemos fazer o seguinte, se o erro foi ValueError, erro de valor ou erro de tipo.
# Podemos colocar entre parênteses quando temos mais de um erro para um except.

# (...)
# except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')
# (...)

# Assim podemos ter outros excepts com os tipos da exceção e a mensagem personalizada:

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')
# except ZeroDivisionError:
#     print('Não é possível dividir um número por zero!')
# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados!')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')

# É possível também fazer um try para cada linha no código, ação, se não conseguir dá um
# determinado erro.
# Por exemplo tenta ler a variável a, se não dá um determinado erro, depois tenta ler a
# variável b, mesma coisa, e depois tenta dividir a por b.

# Então cada 'linha de código' pode ter um bloco try, apesar de o código ficar muito grande.

# Sempre experimente o programa pelo 'certo', digitando dois números inteiros nesse caso:

# Vamos ver então se o 'certo' está funcionando:

# Numerador: 7
# Denominador: 3
# O resultado é 2.3
# Volte sempre! Muito obrigado!

# Agora vamos tentar forçar erros:

# Numerador: 7
# Denominador: 0
# Não é possível dividir um número por zero!
# Volte sempre! Muito obrigado!

# Já conseguimos colocar um erro mais personalizado.


# Numerador: 8
# Denominador: dois
# Tivemos um problema com os tipos de dados que você digitou.
# Volte sempre! Muito obrigado!


# Vamos tentar deixar vazio o primeiro número:

# Numerador:
# Tivemos um problema com os tipos de dados que você digitou.
# Volte sempre! Muito obrigado!


# Pode digitar 200, e aí não quer mais digitar o denominador, pode digitar Ctrl+C no teclado,
# ou vai no PyCharm e aperta o botão vermelho de 'stop', e aí ocorre a exceção do
# KeyboardInterrupt.

# Numerador: 200
# Denominador: O usuário preferiu não informar os dados!
# Volte sempre! Muito obrigado!


# Agora não há mais aquelas mensagens de erro, e inclusive é possível até fazer um erro
# genérico.

# É possível fazer isso durante o desenvolvimento para sempre mostrar o erro, por exemplo
# pode colocar a causa, assim será mostrado a causa do erro na tela quando o except genérico
# ocorrer.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
