def leia_int(msg):
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
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for num, item in enumerate(lista, 1):
        print(f'\033[33m{num}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leia_int('\033[32mSua opção: \033[m')
    return opc
