cor = {'brn': '\033[1;30m',
       'azcn': '\033[1;36m',
       'rn': '\033[1;35m',
       'azmn': '\033[1;34m',
       'l': '\033[m'}

print('==' * 26)
print(cor['brn'] + 'Conversor de graus Celsius para Fahrenheit e Kelvin' + cor['l'])
print('==' * 26)
c = float(input('\nInforme a temperatura em °C: '))  # Graus Celsius(°C)
f = c * 9 / 5 + 32  # Graus Fahrenheit(°F). Pesquisei e "(c * 9 / 5) + 32", mas e a ordem de precedência...?! - trabalho
k = c + 273.15  # Kelvin (K).
print('\nA temperatura de {}{} °C{} equivale a {}{} °F{} e {}{} K{}.'.format(cor['azcn'], c, cor['l'], cor['rn'], f,
                                                                             cor['l'], cor['azmn'], k, cor['l']))
