def aumentar(valor=0, taxa=0, formatc=False):
    """
    -> Aumenta um valor em uma dada porcentagem.

    Parâmetros opcionais
    :param valor: Valor monetário
    :param taxa: Número da porcentagem
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: valor com aumento da porcentagem com a formatação ou não.
    """
    res = valor + (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def diminuir(valor=0, taxa=0, formatc=False):
    """
    -> Diminui um valor em uma dada porcentagem.

    Parâmetros opcionais
    :param valor: Valor monetário
    :param taxa: Número da porcentagem
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: valor com subtração da porcentagem com a formatação ou não.
    """
    res = valor - (valor * (taxa / 100))
    return res if formatc is False else moeda(res)


def dobro(valor=0, formatc=False):
    """
    -> Dá o dobro de um valor.

    Parâmetros opcionais
    :param valor: Valor que será dobrado.
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: Valor dobrado com a formatação ou não.
    """
    res = valor * 2
    return res if not formatc else moeda(res)


def metade(valor=0, formatc=False):
    """
    -> Dá a metade de um valor.

    Parâmetros opcionais
    :param valor: Valor que será dobrado.
    :param formatc: Booleano que indica se a formatação no valor será feita

    :return: Valor dividido em dois com a formatação ou não.
    """
    res = valor / 2
    return res if not formatc else moeda(res)


def moeda(valor=0., moeda='R$'):
    """
    -> Formata um dado valor monetário.

    Parâmetros opcionais
    :param valor: Valor que será formatado.
    :param moeda: Símbolo.

    :return: Valor formatado com vírgula se for reais, senão com ponto.
    """
    res = f'{moeda}{valor:.2f}'
    return res.replace('.', ',', 1) if moeda == 'R$' else res


def resumo(valor=0, aumento=0, reducao=0):
    """
    -> Aplica várias funções a um valor monetário e mostra os resultados em uma tabela
    formatados.

    Parâmetros opcionais
    :param valor: Valor monetário.
    :param aum: Aumento de porcentagem que será calculado na função aumentar.
    :param red: Redução de porcentagem que será calculado na função diminuir.

    :return: Sem retorno
    """
    print('-' * 32)
    print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado |  {moeda(valor):<9} |')
    print(f'| Metade do preço |  {metade(valor, True):<9} |')
    print(f'| Dobro do preço  |  {dobro(valor, True):<9} |')
    print(f'| {aumento:>3}% de aumento |  {aumentar(valor, aumento, True):<9} |')
    print(f'| {reducao:>3}% de redução |  {diminuir(valor, reducao, True):<9} |')
    print('-' * 32)
