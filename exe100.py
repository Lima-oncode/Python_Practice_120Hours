# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteia(num):
    for x in range(0,5):
        num.append(randint(0, 10))
    print(f'Os números sorteados foram {num}')


def somaPar(num):
    soma_p = 0 
    for x in num:
        if x % 2 == 0:
            soma_p += x
    print(f'A soma dos números pares é {soma_p}')

sorteia(numeros)
somaPar(numeros)
    

# Resolução do professor

def sorteia1(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')
        
def somaPar1(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = []
sorteia1(números)
somaPar1(números)   