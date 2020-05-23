from ex108.moeda import moeda


def aumentar(valor, porcentagem, formatação):
    r = valor + (valor * (porcentagem / 100))
    return moeda(r) if formatação else r


def diminuir(valor, porcentagem, formatação):
    r = valor - (valor * (porcentagem / 100))
    return moeda(r) if formatação else r


def dobro(valor, formatação):
    r = valor * 2
    return moeda(r) if formatação else r


def metade(valor, formatação):
    r = valor / 2
    return moeda(r) if formatação else r
