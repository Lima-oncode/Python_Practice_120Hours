# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

max_second_row = third_column = sumpar =  0
mat = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        mat[linha][coluna] = int(input(f'Preencha a posição [{linha}, {coluna}]: '))
        if mat[linha][coluna] % 2 == 0:
            sumpar += mat[linha][coluna]
        if coluna == 2:
            third_column += mat[linha][coluna]
        if linha == 1:
            if mat[linha][coluna] > max_second_row:
                max_second_row = mat[linha][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{mat[linha][coluna]:^7}]', end='')
    print()

print(f'A soma de todos os valores pares é {sumpar}')
print(f'A soma dos valores da terceira coluna é {third_column}')
print(f'O maior valor da segunda linha é {max_second_row}')

# Resolução do professor


matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = scol = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

