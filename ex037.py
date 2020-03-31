n = int(input('\nDigite um número inteiro: '))
print('''\nEscolha uma das bases para conversão:\n
\033[1;32m[ 1 ]\033[m converter para \033[1;32mBINÁRIO\033[m;
\033[1;34m[ 2 ]\033[m converter para \033[1;34mOCTAL\033[m;
\033[1;35m[ 3 ]\033[m converter para \033[1;35mHEXADECIMAL\033[m.''')
bc = int(input('\nSua opção: '))  # Base de conversão

if bc == 1:
    print('\n{} em \033[1;32mBINÁRIO\033[m é \033[1;32m{}\033[m.'.format(n, bin(n)[2:]))
elif bc == 2:
    print('\n{} em \033[1;34mOCTAL\033[m é \033[1;34m{}\033[m.'.format(n, oct(n)[2:]))
elif bc == 3:
    print('\n{} em \033[1;35mHEXADECIMAL\033[m é \033[1;35m{}\033[m.'.format(n, hex(n)[2:]))
else:
    print('\n\033[1;31mOpção inválida. Tente novamente.')
