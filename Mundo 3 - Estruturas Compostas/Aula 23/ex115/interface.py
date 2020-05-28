cores = {
    '': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m'
}


def leia_int(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: por favor, digite um número inteiro válido.', cor='vermelho'))
        except KeyboardInterrupt:
            print(cor(txt='\nO usuário preferiu não informar o valor.', cor='vermelho'))
            return 0
        except Exception as erro:
            print(cor(txt=f'ERRO: {erro.__cause__}', cor='vermelho'))
        else:
            return valor


def linha(tam=40):
    print('-' * tam)


def titulo(msg):
    linha()
    print('|', msg.center(36), '|')
    linha()


def cor(txt='', cor=''):
    return f'{cores[cor]}{txt}{cores[""]}'


def menu(*opcs):
    titulo('MENU PRINCIPAL')
    for n, item in enumerate(opcs, 1):
        print('|', f"{cor(txt=n, cor='amarelo')} - {cor(txt=item, cor='azul')};".ljust(56), '|')
    linha()
    opc = leia_int('Opção: ')
    while opc not in range(1, len(opcs) + 1):
        if opc not in range(1, len(opcs) + 1):
            print(cor(txt='ERRO! Digite uma opção válida!', cor='vermelho'))
        opc = leia_int('Opção: ')
    return opc
