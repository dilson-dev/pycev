# Exercício Python #008 - Conversor de Medidas
print('=-' * 20)
print('\033[1;31mConversor de metros p/ outras medidas.\033[m')
print('=-' * 20)
m = float(input('\n\033[1;36mDigite uma medida em metros: \033[m'))
print('\n\nA medida de {}{}m{} equivale a:'.format('\033[1;30m', m, '\033[m'))
print('\n{}{}km'.format('\033[1;7;30m', m / 1000))
print('{}{}hm'.format('\033[1;7;31m', m / 100))  # Hectômetro
print('{}{}dam'.format('\033[1;7;32m', m / 10))  # Decâmetro
print('{}{:.0f}dm'.format('\033[1;7;33m', m * 10))  # Decímetro
print('{}{:.0f}cm'.format('\033[1;7;34m', m * 100))
print('{}{:.0f}mm'.format('\033[1;7;35m', m * 1000))
print('{}{:.0f}μm'.format('\033[1;7;36m', m * 1000000))  # Micrômetro
print('{}{:.0f}nm'.format('\033[1;7;37m', m * 1000000000))  # Nanômetro
