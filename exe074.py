# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(tupla)
print('O maior valor gerado foi {}'.format(max(tupla)))
print('O menor valor gerado foi {}'.format(min(tupla)))

# Resolução do professor

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valors sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O maior valor sorteado foi {min(numeros)}')
