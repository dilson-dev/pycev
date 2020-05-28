def leia_int(msg):
    """
    -> Valida valores do tipo inteiro.
    :param msg: Mensagem que será exibida para entrada do valro inteiro
    :return: Valor inteiro
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    """
    -> Retorna uma linha.
    :param tam: quantidade de dashes que a linha terá
    :return: linha
    """
    return '-' * tam


def cabeçalho(txt):
    """
    -> Cria um texto centralizado com linhas acima e abaixo.
    :param txt: Texto que será exibido entre as linhas
    :return: Sem retorno
    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    -> Faz um menu com as opções passadas e retorna a opção que usuário escolher.
    :param lista: opções que serão colocadas no menu.
    :return: opção escolhida pelo usuário.
    """
    cabeçalho('MENU PRINCIPAL')
    for num, item in enumerate(lista, 1):
        print(f'\033[33m{num}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leia_int('\033[32mSua opção: \033[m')
    return opc
