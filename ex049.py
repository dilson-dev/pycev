# Tabuada v2.0

n = int(input('{}\nDigite um número: '.format('\033[1;30m')))
print('\n{}Tabuada do número {}:{}\n'.format('\033[1;36m', n, '\033[m'))
print('\033[1;37m' + '-' * 12)
for c in range(11):
    print(f'\033[1;30m{n} x {c:2}\033[35m = \033[32m{n * c}')
print('\033[1;37m' + '-' * 12)
