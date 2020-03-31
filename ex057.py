"""
Desafio 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""

genero = input('\nGênero [M/F]: ').strip().upper()  # [0]
generos = ['M', 'MASCULINO', 'HOMEM', 'MENINO', 'F', 'FEMININO', 'MULHER', 'MENINA']  # 'MmFf' 'M ..'
while genero not in generos:  # or genero == ''
    genero = input('\nDados inválidos. Informe seu gênero: ').strip().upper()

generopos = generos.index(genero)

print(f'\nGênero {"Masculino" if generopos <= 3 else "Feminino"} registrado com sucesso.')
