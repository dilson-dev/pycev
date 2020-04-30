# Python Exercício #041 - Classificando Atletas
from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {} anos.\nClassificação: '.format(idade), end='')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JÚNIOR.')
elif idade <= 25:
    print('SÊNIOR')
else:  # elif idade > 25:
    print('MASTER')
