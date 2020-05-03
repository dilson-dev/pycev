# Curso Python #09 - Manipulando Texto
# Curso Python #09 - Manipulating Text


frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])  # Output 'e'.
# Mostra o 2° elemento de 3, pois começa com 0 (Curso) na lista (splitado) e 3° letra com mesma ideia de antes inicia 0
# Portanto, a letra e mostrado é a letra 'e' que aparece em 'Vídeo'.

''' 
frase.replace('Python', 'Android')  String é em si imutável, não funciona Frase[0] = J p/ trocar 1° letra por J.
print(frase) Irá ser a frase normal sem replace, a não ser que frase seja atribuída ao replace, aí sim irá mudar.
print('Curso' in frase) True or False
print(frase.find('Curso',))  # Posição do n° que começa, nesse caso 0. Se não tiver irá aparecer -1.
print(frase.lower().find('vídeo'))  # Sem lower ele não aparece 9, aparece -1. 

-1 significa que a string colocada no argumento da função não foi encontrada na frase.
'''


'''
frase = '   Curso em Vídeo Python   '
print(frase.upper().count('O')) Combina duas funcionalidades
print(len(frase.strip())) 
'''


# 3 aspas podem ser usadas tanto no print como para comentários.

'''
print("""
skaldjaskdj
aslkdjaskdjasldja
skdjaslkdskaldjaskdja
slkdjask
djasldjaskdja
""")
'''