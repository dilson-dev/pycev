# Exercício Python #101 - Funções para votação

"""
DESAFIO 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

# from datetime import date


def voto(nasc):
    """
    -> Calcula a condição de voto a partir do ano de nascimento de uma pessoa.
    :param nasc: Ano de nascimento da pessoa.
    :return: Idade com a condição de voto.
    """

    from datetime import date

    ano = date.today().year
    idade = ano - nasc

    if idade < 16:
        cond = 'NEGADO'  # cond = 'NÃO VOTA'
    elif idade < 18 or idade > 65:
        cond = 'OPCIONAL'  # cond = 'VOTO OPCIONAL'
    else:
        cond = 'OBRIGATÓRIO'  # cond = 'VOTO OBRIGATÓRIO'

    return f'Com {idade} anos: VOTO {cond}.'


# Programa Principal

help(voto)

print('\n', '-' * 40, sep='')
nascimento = int(input('Ano de nascimento (formato AAAA): '))

print(voto(nascimento), end='\n\n')
help(voto)

# Escopo de importação

# É possível importar a biblioteca no programa principal, porém será importado para o programa
# inteiro, sendo possível criar uma variável para o mês, por exemplo:
# mês = date.today().month
# Só que não tem importância o uso da biblioteca no programa principal, mas sim na função.
# Por isso pode fazer a importação exatamente dentro da def.
# Ao importar dentro de uma função a importação só serve para dentro dela, economizando
# memória. Assim a classe date só ficará na memória durante a execução da função, e não fora
# economizando bastante.
# Portanto é interessante fazer isso caso o que esteja importando seja necessário apenas
# dentro de uma função.


# Conforme solução do vídeo:
'''
def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
'''
