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

    :return: Valor formatado.
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',', 1)
