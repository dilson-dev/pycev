# Código principal

'''
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
'''
# Retorna um erro porque as funções estão no outro arquivo.

# Para resolver isso usaremos um comando que já foi muito usado, o import.
# Na aula 8 foi falado de módulos que já existem/vem no Python, só precisando importar.

# Mas nem tudo existe/vem no Python, tem que coisa que não foi criada ainda.
# Assim é possível criar seus próprios módulos.

'''
import uteis
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
'''

# Para o Python todo arquivo com extensão py pode ser um módulo, contanto que tenha
# funções internas, e esse é o conceito de modularização.

# Só que import uteis não funciona ainda, pois não está utilizando as funções de uteis.py
# Para fazer isso colocamos uteis antes do nome das funções com um ponto (uteis.func()):

'''
import uteis
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
'''

# PyCharm mostra as funções de dentro de uteis ao escrever 'uteis.', em ordem alfabética.

# O código está funcional, e de quebra não está tão grande como estava com tudo em um
# arquivo py só.

# Assim colocamos no arquivo principal aquilo que é usado diretamente, e as funções ficam
# em um outro arquivo. Isso simplifica o código.

# No código principal não é necessário ver como as funções funcionam, mas saber que elas
# estão ali no código. Por exemplo ao importar a função sqrt de math que retorna a raiz
# quadrada de um número não foi necessário saber como foi esse cálculo, a única coisa
# necessária foi saber o que esta função faz.

# Nessa situação é a mesma coisa, não é necessário saber como foi calculado o fatorial
# e dobro, só é necessário saber que foi escrito o código e este está disponível para
# fazer determinada coisa.

# É possível também importar as funções diretamente c/ from <módulo> import <func1>, <f2>
'''
from uteis import fatorial, dobro
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
'''

# Ao importar as funções diretamente do módulo não é mais necessário usar 'uteis.' antes
# das funções.

# OBS: Essa forma de importação não é tão recomendada, pois pode gerar problemas.
# Podem ocorrer conflitos ao importar funções de mesmo nome.
# Suponha que tivesse outro módulo chamado matematica.py, e nele também tenha uma função
# de dobro.

# Se fizer a importação com o from, pegando o módulo dobro de matematica.py e uteis.py,
# irá acabar confundindo o Python, que não saberá qual função deve executar.
# (Nessa situação a última função importada sobrepõe as outras de mesmo nome)


# from uteis import dobro
# from matematica import dobro
# (função dobro de matematica sobrepõe a de uteis, pois foi a último a ser importada)


# Dessa maneira ficaria mais claro se fizesse apenas o import dos dois módulos:

# import uteis
# import matematica


# Assim é possível diferenciar as funções com mesmo nome que os dois módulos têm, e
# usar ambas, sem as sobrepor e criar conflitos:

# uteis.fatorial()
# matematica.fatorial()


# Deixamos o código apenas com o import do módulo p/ evitar essas incompatibilidades:
'''
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
'''

# Essa é a maneira mais recomendada, embora a versão com o from também funcione sem
# problema nenhum, a questão é o conflito.

# A sintaxe usada na importação c/ from é muito parecida c/ a usada p/ funções externas:

# from uteis import fatorial

# from math import sqrt
# from datetime import datetime
# from random import randint

# from <módulo> import <função>

# As 3 linhas de baixo já eram módulos que vinham no Python, e a primeira linha é uma
# chamada a um módulo criado localmente, por nós mesmos, o módulo uteis.

# Esse é o conceito básico de modularização.


# Vantagens da modularização:
# - Organização do código (divide um problema maior em menores);
# - Facilidade na manutenção (se alguma função parar de funcionar, ou pensar numa solução
# melhor p/, é só entrar no módulo específico e alterar a função, e todos os locais
# que utilizarem esta função irão se beneficiar desta nova versão desta.);
# - Ocultação de detalhes do código (Não é necessário saber como fazer o que a função
# faz, mas saber que a função faz determinada coisa. Não se preocupa com as funções)
# - Reutilização em outros projetos (Reutilizar módulos em outros projetos copiando
# o arquivo do módulo e jogando na pasta de outro projeto e todas as funções estarão
# disponíveis ali para serem importadas caso sejam necessárias).


# Módulos são muito importantes quando começamos a crescer os programas, mas quando os
# módulos não derem mais conta do trabalho há uma solução no Python chamada de Pacotes.
# Algumas outras linguagens de programação chamam isso de Biblioteca.
# O Python chama isso de Pacotes ou Packages, em inglês.


# PACOTES Prática

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')


# Dividimos assim o nosso problema em problemas menores.

# Como irá começar a desenvolver coisas maiores em Python é interessante se aprofundar.
# Conhecer o uso de padrão de pacotes, organização de pacotes, o uso de init é muito
# importante.
