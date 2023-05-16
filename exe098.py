# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem.

# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador (inicio, fim, passo):
    for x in range(inicio, fim+1, passo):
        print(f'{x} ', end='', flush=True)
        sleep(0.2)
        
print('a) De 1 até 10, de 1 em 1')
contador(1, 10, 1)


print('\nb) De 10 até 0, de 2 em 2')
contador(10, 0, -2)


print('\nc) Uma contagem personalizada')
contador(0, 100, 10)

# Segunda forma de resolução

def contador (inicio, fim, passo):
    for x in range(inicio, fim+1, passo):
        print(f'{x} ', end='', flush=True)
        sleep(0.2)

inicio_a = 1
fim_a = 10
passo_a = 1
        
print('a) De 1 até 10, de 1 em 1')
contador(inicio_a, fim_a, passo_a)

inicio_b = 10
fim_b = 0
passo_b = -2

print('\n\nb) De 10 até 0, de 2 em 2')
contador(inicio_b, fim_b, passo_b)

inicio_c = 0
fim_c = 100
passo_c = 10

print('\n\nc) Uma contagem personalizada')
contador(inicio_c, fim_c, passo_c)

# Resolução do professor

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i}, até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}  ', end='', flush=True)
            sleep(0.5)
            cont = cont - p
        print('FIM')
        
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
        
    