#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base da conversão :
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# O Sistema binário é a representação de todos os números do computador
# Os novos números de IP são todos hexadecimais
# Alguns sistemas de erro são representado por sistema octal

# Sistema decimal 0 - 9
# Sistema binário 0 e 1
# Sistema Octal   0 - 7
# Sistema Hexadecimal 0 - 9 e A - F


numero = int(input('Digite um número inteiro: '))
print('Agora escolha a base de conversão!')
print(' 1 - Binário | 2 - Octal | 3 - Hexadecimal ')
conversao = int(input(': '))

if conversao   == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('{} convertido para hexadeciamal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Você deve escolhar uma opção válida!')

# Resolução do professor

num = int(input('Digite um número inteiro: '))
print
('''
Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadeciamal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')





