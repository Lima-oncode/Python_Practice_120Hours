# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Verificação de número primo no modo mais simples é verificar se a sobra da divisão ocorre mais de duas vezes

# DIC.CORES

vermelho = '\033[31m'
verde = '\033[32m'


n  = int(input('Digite um número inteiro: '))
inicio = 1
fim = n + 1
count = 0 

for i in range(inicio, fim):
    if n % i == 0:
        count += 1
if count > 2:
    print('NÃO É PRIMO!')
else:
    print('É PRIMO!')

# Resolução do professor

num = int(input('Digite um número: '))
tot = 0 
for c in range(1, num + 1):
    if num % c == 0:
        print(verde, end='')
        tot += 1
    else:
        print(vermelho, end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

        

