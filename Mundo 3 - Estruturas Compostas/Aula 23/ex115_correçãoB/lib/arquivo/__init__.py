from lib.interface import cabeçalho


def arquivo_existe(nome):
    """
    -> Verifica se existe um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo
    :return: True se existe, False se não existe.
    """
    try:
        a = open(nome, 'rt')  # rt = read text = Leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Função open tenta abrir um arquivo, o 'rt' significa leitura de arquivo texto, que é read text.
# a.close() fecha o arquivo.


def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo de texto
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+')  # wt+ = write text O + de 'wt' que cria o arquivo.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    """
    -> Lê o conteúdo de um arquivo de texto.
    :param nome: Nome do arquivo de texto.
    :return: Sem retorno.
    """
    try:
        a = open(nome, 'rt', encoding='utf-8')
        # Especifiquei encoding, pois os acentos não estão sendo exibidos no PyCharm.
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        # print(a.readlines())  # Mostra tudo em uma linha mostrando as quebras de linha \n
        print(a.read())
