from lib.interface import cabeçalho


def arquivo_existe(nome):
    """
    -> Verifica se existe um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo
    :return: True se existe, False se não existe.
    """
    try:
        a = open(nome, 'rt', encoding='utf-8')  # rt = read text = Leitura de arquivo texto
        a.close()

        # Especifiquei encoding, pois os acentos não estão sendo exibidos no PyCharm.

        # Função open tenta abrir um arquivo, o 'rt' significa leitura de arquivo texto, que é read text.
        # a.close() fecha o arquivo.

    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo de texto
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+', encoding='utf-8')  # wt+ = write text O + de 'wt' que cria o arquivo.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
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
    except:
        print('Erro ao abrir o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')

        # print(a.readlines())
        # Mostra o conteúdo inteiro do arquivo de texto em uma única linha, inclusive com as quebras
        # de linha (\n).

        # print(a.read())
        # Mostra o conteúdo inteiro do arquivo formatado com as quebras de linha.

        for linha in a:
            dado = linha.split(sep=';')  # Separa a linha por ponto e vírgula.
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    """
    -> Insere o nome e idade de uma pessoa em um arquivo de texto.
    :param arq: Nome do arquivo em que será salvo os dados.
    :param nome: (opcional) Nome da pessoa que será salvo.
    :param idade: (opcional) Idade da pessoa que será salvo.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao cadastrar os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
