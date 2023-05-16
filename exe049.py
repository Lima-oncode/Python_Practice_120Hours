# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
# um laço for.

t = int(input('Digite algum número para ver sua tabuada: '))
for x in range(10, 0, -1):
    print('A tabuada de {} * {} é igual a {}'.format(t, x, t * x))

# Resolução do professor

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))