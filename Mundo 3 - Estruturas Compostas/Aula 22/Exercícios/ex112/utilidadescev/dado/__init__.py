def leia_dinheiro(msg):
    valor = -1
    while not str(valor).replace('.', '', 1).isdigit():
        valor = input(msg).replace(',', '.', 1)
        if not str(valor).replace('.', '', 1).isdigit():
            print(f'\033[1;31mERRO! "{valor}" é um preço inválido!\033[m')
    return float(valor)
