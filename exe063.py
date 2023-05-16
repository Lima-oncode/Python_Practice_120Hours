# Escreva um programa que leia n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
# de Fibonacci
# Ex. 0 - 1 - 1 - 2 - 3 - 5 - 8

# Para a realização deste exercício é importante entender a lógica. Considerando que 'p' é a posição 
# na sequencia. Entenda que p1 passa a ser p2 e p2 passa a ser o resultado de p1 + p2 ou seja p2 = p3 após
# o calculo da terceira posição

p1 = 0
p2 = 1
elementos = int(input('Digite quantos elementos deseja visualizar'))
count = 3
print('{} > {} > '.format(p1, p2), end='')
while count <= elementos:
    p3 = p1 + p2
    print('{} > '.format(p3), end='')
    p1 = p2
    p2 = p3
    count += 1
print('FIM')

# Resolução do professor

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} > {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~'*30)

