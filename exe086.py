# Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela com a formatação correta.

mat = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        mat[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print(f' {mat[0]} \n {mat[1]} \n {mat[2]} ')

# Resolução do professor

# Repetições 'for' para alimentar a matriz
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite para a posição [{l}, {c}]: '))

# Repetições 'for' para apresentar a estrutura de forma formatada
for l in range(0, 3):
    for c in range(0, 3):
        # ':^5' comando para centralizar utilizando 5 posições
        print(f'[{matriz[l][c]:^5}]', end='')
    # print para realizar a quebra de linha em cada iteração
    print()
