# # Faça um programa que leia um número qualquer e mostre o seu fatorial. 

# num = int(input('Digite um número inteiro: '))
# resultado = 1
# count = 1

# while count <= num:
#     resultado = resultado * count
#     count = count + 1
# print('O fatorial de {} é {}!'.format(num, resultado))

# # 2° Resolução

# num = int(input('Digite um número para calcular seu Fatorial: '))
# c = num
# fat = 1

# while c > 0:
#     fat = fat * c
#     c = c - 1
# print('O fatorial de {} é {}'.format(num, fat))

# # 3° Resolução (Utilizando o for)
# # A variável é a principal jogada do teste de fatorial pois ela recebe o resultado da interação e a refaz
# # utilizando o resultado da operacao antecessora

# n = int(input('Digite um número inteiro e veja seu fatorial: '))
# resultado = 1

# for f in range(1, n+1):
#     resultado = resultado * f
#     print(resultado) 

# # Resolução do professor

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))

# 2° Resolução do professor

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


