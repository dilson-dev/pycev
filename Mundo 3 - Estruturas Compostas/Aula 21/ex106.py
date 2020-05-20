# Exercício Python #106 - Sistema interativo de ajuda em Python
# Python exercise #106 - Interactive helping system in Python

"""
DESAFIO 106
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
"""

from time import sleep


def ajuda(com):
    """
    -> Exibe a ajuda interativa de um "comando" do Python.
    :param func: (Obrigatório) Função que será exibida a ajuda interativa do Python.
    :return: Sem retorno.
    """

    título(f'Acessando o manual do comando \'{com}\'', cor='azul')
    print(cores['branco'])
    help(com)
    print(end=cores['sem'])
    sleep(2)


def título(msg, cor='sem'):
    """
    -> Escreve um título com a cor desejada na tela.
    :param msg: (obrigatório) A mensagem que será exibida na tela.
    :param cor: (opcional) A cor em que o texto será exibido.
    :return: Sem retorno.
    """
    tam = len(msg) + 6
    print(end=cores[cor])
    print('~' * tam)
    print(f'|  {msg}  |')
    print('~' * tam)
    print(end=cores['sem'])
    sleep(1)


# Programa Principal

# Definição de cores conforme o vídeo da solução, usando tuplas:
'''
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;3045m',    # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )
'''

cores = {'sem': '\033[m',  # Limpa cor
         'vermelho': '\033[1;41m',
         'verde': '\033[1;42m',
         'azul': '\033[1;44m',
         'branco': '\033[7m'
         }

# As cores são feitas através do padrão ANSI, não precisando carregar bibliotecas.

while True:
    título('SISTEMA DE AJUDA PyHELP', cor='verde')
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)

título('ATÉ LOGO!', cor='vermelho')
