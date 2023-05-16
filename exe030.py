# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar!')

# Resolução do professor

número = int(input('Digite um número qualquer: '))
resultado = número % 2 
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))

