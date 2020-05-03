# Exercício Python #024 - Verificando as primeiras letras de um texto
cidade = str(input('\033[1;30mDigite o nome de uma cidade: ')).strip()
print('\033[1;35mO nome da cidade digitado começa com a palavra \"Santo\"? {}.'.format(
    cidade[:5].lower() == 'santo'))

"""
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
"""
