# Curso Python #012 - Condições Aninhadas

nome = str(input('Qual é seu nome? '))
if nome == 'Delfino':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popualr no Brasil.')
elif nome in ['Ana', 'Cláudia', 'Jéssica', 'Juliana']:  # 'Ana Cláudia Jéssica Juliana':
    print('Você tem um belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
