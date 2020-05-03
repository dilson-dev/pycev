# Código copiado externamente
# Algumas mudanças feitas, inverti os nomes dados e respostas, e dados passou de uma lista para um dicionário.

dados = {
    'somaIdade': 0,
    'idadeHomi+vei': 0,
    'moças': 0,
    'nomeHomi+vei': ''
}

nome, idade, sexo = [], [], []

generos = 'Masculino Homem Menino Feminino Mulher Menina'

print('Informe os seguintes dados de quatro pessoas diferentes:')

for resposta in range(4):
    nome += [input('Nome: ').strip()]
    idade += [input('Idade: ').strip()]
    sexo += [input('Sexo: ').strip().upper()]
    print('-' * 10)
    if sexo[resposta] in generos:
        if generos.find(sexo[resposta]) < 23:
            sexo[resposta] = 'M'
        else:
            sexo[resposta] = 'F'
    else:
        sexo[resposta] = 'Error'
    if idade[resposta].isnumeric():
        idade[resposta] = int(idade[resposta])
        dados['somaIdade'] += idade[resposta]
        if sexo[resposta] == 'M' and (idade[resposta] > dados['idadeHomi+vei'] or resposta == 0):
            dados['idadeHomi+vei'] = idade[resposta]
        elif sexo[resposta] == 'F' and idade[resposta] < 20:
            dados['moças'] += 1
    else:
        idade[resposta] = 'Error'
        break

if ('Error' in idade) or ('Error' in sexo):
    print('Erro: Alguma idade ou sexo está incorreta leia as instruções e certifique-se de informar os dados '
          'corretamente.')
else:
    for i in range(4):
        if sexo[i] == 'M' and idade[i] == dados['idadeHomi+vei']:
            dados['nomeHomi+vei'] += nome[i]
    print(f'Média de idade do grupo: {dados["somaIdade"] / 4} anos;\n'
          f'Nome homem mais velho e idade: {dados["nomeHomi+vei"]}, {dados["idadeHomi+vei"]} anos;\n'
          f'Quantidade de moças abaixo de 20 anos: {dados["moças"]}.')
print('=' * 60)
