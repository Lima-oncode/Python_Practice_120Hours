# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato

total = mil = count = 0
nomebarato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto R$ '))
    count += 1
    total += preco
    if preco > 1000:
        mil += 1
    if count == 1:
        barato = preco
    else:
        if preco < barato:
            barato = preco
            nomebarato = produto
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(
f''' 
O total da compra foi R${total}
Temos {mil} produtos custando mais de R$1000.00
O produto mais barato foi {nomebarato} que custa R${barato}
''')

# Resolução do professor

total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        totmil += 1
    if count == 1 or preco < menor:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')