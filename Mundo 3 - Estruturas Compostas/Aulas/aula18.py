# Curso Python #17 - Listas (Parte 2)

galera = list()  # Estrutura principal
dados = list()  # Estrutura auxiliar p/ pegar os dados p/ depois colocá-los na estrutura principal
totmai = totmen = 0

print()

# Lê os dados e joga dentro de galera
for c in range(3):
    print('=-' * 16)
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()  # dados = list()

print('=-' * 16)

# Analisa os dados conforme a idade
for pessoa in galera:
    # print(f'{pessoa[0]} é', 'maior'if pessoa[1] >= 21 else 'menor', 'de idade.')
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmai += 1
    else:
        print(F'{pessoa[0]} é menor de idade.')
        totmen += 1

print('=-' * 16, f'{totmai} maior(es) e {totmen} menor(es) de idade.', '=-' * 16, sep='\n')
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera)  # Mostra toda a estrutura com todos os colchetes.
# print(galera[0])  # Mostra somente os dados da lista no índice 0, nesse caso ['João', 19]
# print(galera[0][0])  # Mostra valor do índice 0 da lista no índice 0, nesse caso João
# print(galera[2][2])  # 13
print()
# print([galera[n][0] for n in range(4)], [galera[n][1] for n in range(4)])
for dados in galera:
    # print(dados) Imprime cada lista em uma linha.
    # dados[0] Somente os nomes
    # dados[1] Somente as idades
    print(f'{dados[0]} tem {dados[1]} anos.')
'''
"""
teste = list()
teste.append('Gustavo')
teste.append(40)  # teste = ['Gustavo', 40]
galera = list()
galera.append(teste[:])  # galera = [['Gustavo', 40]]  # galera.append(teste) cria ligação
teste[0] = 'Maria'  # teste = ['Maria', 40]
teste[1] = 22  # teste = ['Maria', 22]
galera.append(teste[:])
'''
galera = [['Gustavo', 40], ['Maria', 22]]  
Ao usar append na lisa galera fica com duas Marias 22.
Para corrigir isso deve fazer uma cópia de teste, e não dar o append na própria lista em si, se não é criada a ligação
com a estrutura, e ao mudar teste, é mudado dentro de galera também.
'''
print(galera)
"""
