# Exercício Python #099 - Função que descobre o maior

"""
DESAFIO 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

# Notas:

# Segundo Guanabara teve algumas alterações no PyCharm de versões anteriores para a versão 2018.2.3
# (no momento em que estava gravando). Teve uma pequena mudança que tornaria necessário o uso do
# parâmetro flush na função print usada em conjunto com a função sleep.

# Testei na versão do PyCharm de 2020 e isso parece que foi revertido.
# Nas primeiras execuções do código sem o flush havia um pouco de lag, por isso acontecia de pular o
# sleep, mas na terceira ou quarta ele já exibia o código de maneira linear.

# No meu caso, eu uso o parâmetro flush para executar o código no terminal.


from time import sleep


def maior(* núms):
    # 1ª Solução usando a função max:
    '''
    ma = max(nums) if len(nums) > 0 else 0
    print(f'O maior valor é {ma}.')
    '''

    # 2ª Solução sem uso da função max (baseada no vídeo da aula c/ execução do exercício):
    print('-=' * 40)
    print('Analisando os valores passados...')
    sleep(1)

    ma = 0  # cont = ma = 0
    for num in núms:
        print(num, end=' ', flush=True)
        sleep(0.3)

        # Usando núms[0] p/ pegar 1º valor como maior:
        if num == núms[0] or num > ma:
            ma = num

        # Conforme solução do vídeo:
        # if cont == 0 or valor > ma:
        #    ma = valor
        # cont += 1

    if len(núms) != 0:
        print(f'Foram informados {len(núms)} valores ao todo.')
        print(f'O maior valor é {ma}.')
    else:
        print('Nenhum valor informado.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
