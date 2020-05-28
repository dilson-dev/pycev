def registrar(arq, nome='Desconhecido', idade=0):
    try:
        with open(arq, 'a', encoding='utf-8') as f:
            f.write(f'{nome};{idade}\n')
    except:
        print('Houve um erro na hora de registrar os dados.')
    else:
        print(f'Novo registro de {nome} adicionado com sucesso!')


def exibir(arq):
    try:
        with open(arq, 'a+', encoding='utf-8') as f:
            f.seek(0)
            for linha in f:  # f.readlines()
                nome, idade = linha.replace('\n', '').split(';')
                print(f'{nome:<27} {idade:>3} anos')

        # a+ = adição e leitura.
        # É possível criar o arquivo, e caso seja executado outra vez este não é criado novamente.

        # f.seek('posição') = define de qual posição se dará o início da leitura do arquivo de texto.
        # É usado porque o modo de adição joga o pointer (posição) para o fim do arquivo, assim deve
        # colocá-lo para o início, caso contrário não será feita a leitura do arquivo de texto.

    except Exception as erro:
        print('Houve um erro na hora de exibir os dados do arquivo.')
        print(erro.__class__)
