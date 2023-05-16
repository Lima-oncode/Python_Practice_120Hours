# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disto, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados
# respectivamente.
# No final, mostre o conteúdo das três listas geradas.

valores = []
par = []
impares = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impares.append(num)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''\nOs valores digitados foram {valores}. 
Sendo que dentre estes os pares foram {par} e os ímpares foram {impares}''')

# Resolução do professor

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')