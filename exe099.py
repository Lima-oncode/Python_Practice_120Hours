# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    omaior = 0
    print(f'Os valores analisados foram: ')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.2)
        if omaior < n:
            omaior = n
    print(f'\nForam passados {len(num)} valores e o maior valor foi: {omaior}')

maior(8,10,23,25,2,1,93,2,1,124)

# Resolução do professor

def maior1(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
        
                
maior1(2, 9, 4, 5, 7, 1)
maior1(4, 7, 0)
maior1(1, 2)
maior1(6)
maior1()