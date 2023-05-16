# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados de forma tabular.

items = ('celular', '1.300', 'caneta', '3.00', 'regua', '8.00')

for x in range(0, len(items)):
    if x % 2 == 0:
        print(f'{items[x]:.<30}', end='')
    else:
        print(f'R${items[x]:>5}')


# Resolução do professor

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 30)

