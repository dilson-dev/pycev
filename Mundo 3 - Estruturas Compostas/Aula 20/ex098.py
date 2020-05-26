# Exercício Python #098 - Função de Contador

"""
DESAFIO 098
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
"""

from time import sleep


def contador(início, fim, passo):
    passo = 1 if passo == 0 else abs(passo)

    # Mesmo que coloque o passo negativo (-2), a função abs cuida disso, tornando passos negativos em positivos.
    # E independente de ser negativo ou positivo, se o início for maior que o fim, o passo é considerado negativo.

    print('-=' * 25)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}:')

    sleep(1.5)

    # Com for
    if início > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1

    for n in range(início, fim, passo):
        print(n, end=' ', flush=True)
        sleep(0.3)
        # O parâmetro flush=True é para forçar o efeito do sleep na linha de comando, sem este o sleep é 'pulado'.
    print('FIM!')

    # Com while
    '''
    contador = início

    if início < fim:
        while contador <= fim:
            print(contador, end=' ', flush=True)
            sleep(0.3)
            contador += passo
    else:
        while contador >= fim:
            print(contador, end=' ', flush=True)
            sleep(0.3)
            contador -= passo

    print('FIM!')
    '''


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 25)
print('Você que faz a contagem agora!')

while True:
    ini = int(input('Início: '))
    end = int(input('Fim:    '))
    pas = int(input('Passo:  '))

    contador(ini, end, pas)

    print('-=' * 25)

    while True:
        flag = input('Fazer outra contagem? [S/N] ').strip().upper()
        if flag != '' and flag[0] in 'SN':
            break
        print('Erro. Tente novamente.')

    if flag[0] == 'N':
        break
