def aumentar(valor=0, taxa=0, formatc=False):
    """
    -> Calcula o aumento de um valor em uma dada porcentagem,
    retornando o resultado com ou sem formatação.

    Parâmetros opcionais
    :param valor: o valor que se quer reajustar
    :param taxa: porcentagem do aumento
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: valor com reajuste, formatado ou não.
    """
    res = valor + (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def diminuir(valor=0, taxa=0, formatc=False):
    """
    -> Calcula a redução de um valor em uma dada porcentagem,
    retornando o resultado com ou sem formatação.

    Parâmetros opcionais
    :param valor: o valor que se quer reajustar
    :param taxa: porcentagem da redução
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: valor com reajuste, formatado ou não.
    """
    res = valor - (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def dobro(valor=0, formatc=False):
    """
    -> Dá o dobro de um valor.

    Parâmetros opcionais
    :param valor: Valor que será dobrado.
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: Valor dobrado, formatado ou não.
    """
    res = valor * 2
    return res if not formatc else moeda(res)


def metade(valor=0, formatc=False):
    """
    -> Dá a metade de um valor.

    Parâmetros opcionais
    :param valor: Valor que será dobrado.
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: Valor dividido em dois, formatado ou não.
    """
    res = valor / 2
    return res if not formatc else moeda(res)


def moeda(valor=0., moeda='R$'):
    """
    -> Formata um dado valor monetário.

    Parâmetros opcionais
    :param valor: Valor que será formatado.
    :param moeda: Símbolo.

    :return: Valor formatado.
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',', 1)


def resumo(valor=0, aumento=10, reducao=5):
    """
    -> Aplica várias funções a um valor monetário e mostra os resultados em uma tabela
    formatados.

    Parâmetros opcionais
    :param valor: Valor ao qual serão aplicada as funções.
    :param aumento: Aumento de porcentagem que será calculado na função aumentar.
    :param reducao: Redução de porcentagem que será calculado na função diminuir.

    :return: Sem retorno
    """
    print('-' * 32)
    print('|', 'RESUMO DO VALOR'.center(28), '|')  # print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado |  {moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor, True):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor, True):<9} |')
    print(f'| {aumento:>3}% de aumento |  {aumentar(valor, aumento, True):<9} |')
    print(f'| {reducao:>3}% de redução |  {diminuir(valor, reducao, True):<9} |')
    print('-' * 32)

    '''
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'{aumento:>3}% de aumento:\t{aumentar(valor, aumento, True)}')
    print(f'{reducao:>3}% de redução:\t{diminuir(valor, reducao, True)}')
    '''
    # É preciso de mais de uma tabulação \t dependendo do tamanho da mensagem.


# Guanabara usou \t para fazer a tabulação, mas a execução dos scripts no terminal acaba
# bagunçando toda a formatação, porque no CMD e Powershell é dado 8 espaços na
# visualização do Tab nos scripts, é funcional apenas no PyCharm que dá 4 espaços no TAB.
