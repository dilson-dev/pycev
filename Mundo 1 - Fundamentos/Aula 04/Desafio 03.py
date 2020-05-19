# Desafio 03

"""
Crie um script Python que leia dois números e tente mostrar a soma entre eles.
"""

print('=' * 5, 'DESAFIO 03', '=' * 5)
n1 = input('Primeiro número ')
n2 = input('Segundo número ')
print()
print('A soma é', n1 + n2)
print()

# Na verdade o que está fazendo é pegando o n1, o n2, e colando um no outro.

# Isso ocorre porque o input é recebido como um caractere no Python, e ao usar o operador de soma com caracteres
# ocorre a concatenação, que faz exatamente isso, juntar um valor ao outro, ao invés de somá-los.
# Para resolver isso basta fazer com que o input seja recebido como um número, assim usamos o int no input:

print('=' * 5, 'DESAFIO 03', '=' * 5)
n1 = int(input('Primeiro número '))
n2 = int(input('Segundo número '))
print()
print('A soma é', n1 + n2)
