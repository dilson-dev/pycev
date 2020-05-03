# Exercício Python #011 - Pintando Parede
largura = float(input('\033[1;30mLargura da parede em metros: '))
altura = float(input('Altura da parede em metros: \033[m'))
área = largura * altura
tinta = área/2
# print('A dimensão dessa parede é de {}x{}, assim sua área é de {}m²'.format(largura, altura, área))
print('A parede tem uma área de \033[1;34m{}m²\033[m.'.format(área))
print('A quantidade de tinta necessária para pintar essa parede é de \033[1;31m{} litros.'.format(tinta))
# print('Para pintar essa parede você precisará de {} litros de tinta.'.format(tinta))
