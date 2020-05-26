def leia_dinheiro(msg):
    """
    -> Faz a validação de valores monetários.

    :param msg: (obrigatório) Mensagem que será exibida no terminal para entrada do valor.
    :return: Entrada convertida para ponto flutuante.
    """

    # Solução do vídeo com uma validação bastante duvidável:
    '''
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            válido = True
          return float(entrada)
    '''

    # Solução com uma validação completa:
    while True:
        entrada = input(msg).strip().replace(',', '.', 1)
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[m')

    # Como o return já termina a execução da função, o break se torna redundante.


def leiaInt(msg=''):
    """
    -> Valida entradas numéricas do tipo inteiro.

    :param msg: (opcional) Mensagem que será exibida na tela para entrada do valor numérico.
    :return: O valor numérico recebido como caracter transformado em inteiro.
    """
    while True:
        num = input(msg).strip()
        if num.replace('-', '', 1).isdigit():  # .isnumeric()
            return int(num)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

# É possível ir acumulando as funções dentro de um módulo/pacote, essa é a grande vantagem.
