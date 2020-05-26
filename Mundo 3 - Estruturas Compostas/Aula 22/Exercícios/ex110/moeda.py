from ex109.moeda import aumentar, diminuir, dobro, metade, moeda


def resumo(valor, aum, red):
    print('-' * 32)
    print(f'|{"RESUMO DO VALOR":^30}|')
    print('-' * 32)
    print(f'| Preço analisado:   {moeda(valor):<9} |')
    print(f'| Dobro do preço:    {dobro(valor, True):<9} |')
    print(f'| Metade do preço:   {metade(valor, True):<9} |')
    print(f'| {aum}% de aumento:    {aumentar(valor, aum, True):<9} |')
    print(f'| {red}% de redução:    {diminuir(valor, red, True):<9} |')
    print('-' * 32)
