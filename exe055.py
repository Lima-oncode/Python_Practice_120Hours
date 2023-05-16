# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

max = 0
min = 0

for x    in range(1,6):
    peso = float(input('Digite o {}° peso (Kg): '.format(x)))
    if x == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso
print('O maior peso foi {}'.format(max))
print('O menor peso foi {}'.format(min))

# Resolução do professor

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))