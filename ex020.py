from random import shuffle
n1 = str(input('\n\033[1;30mPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
a = [n1, n2, n3, n4]  # Lista de Alunos
shuffle(a)
print('\nA ordem de apresentação será:', end=' ')
print('\033[1;34m' + str(a) + '\033[1;30m' + '.')

'''
Vi uma resolução com a função sample da biblioteca random também, porém ela é mais especifica e escolhe uma 
quantidade a ser sorteada dentro de uma lista. 
Existe também o sorted que pega algo embaralhado e o deixa em sequência.

from random import sample
n1 = str(input('Primeiro: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro: '))
n4 = str(input('Quarto: '))
n5 = str(input('Quinto: '))
n6 = str(input('Sexto: '))
n7 = str(input('Sétimo: '))
n8 = str(input('Oitavo: '))
n9 = str(input('Nono: '))
n10 = str(input('Décimo: '))
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
ordem = sample(lista, k=3)
print(ordem)
'''
