# Exercício Python #040 - Aquele clássico da Média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('\n\033[1;36mMédia\033[m (\033[1m{:.1f}, {:.1f}\033[m) = \033[1;35m{:.1f}\033[m.'.format(n1, n2, média))
"""
print('\nAluno', end=' ')
if média >= 7:
    print('\033[1;32mAPROVADO\033[m!')
elif média < 5:
    print('\033[1;31mREPROVADO\033[m!')
else:  # elif 5 <= média < 7: Torna o programa mais fácil de ser lido.
    print('em\033[1;33m RECUPERAÇÃO\033[m!')
"""

if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
