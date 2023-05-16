'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
#porção inteira'''
#Ex: 6.127 , o numero tem a parte inteira 6
from math import floor
n = float(input('Digite um número qualquer e veja sua porção inteira'))
int = floor(n)
print('A porção inteira do número digitado é {:.0f}'.format(int))

'''Um dos métodos usado pelo professor:
from math import trunc
print('A porção inteira do número digitado é {:.0f}'.format(int, math.trunc(num)))
Também daria para simplificar apenas solicitando o print como int'''
