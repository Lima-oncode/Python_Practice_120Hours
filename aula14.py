# Estrutura de repetição While

'''
# Exemplo para compreensão
enquanto não chegar:
    passo
pega

# Exemplo em Python
while not maça:
    passo
pega

# Exemplo para compreensão 2

enquanto não maça:
    if chao:
        passo
    elif buraco:
        pula
    elif moeda:
        pega
pega
'''

# Ex. 2 Python
'''
while not maça:
    if chao == True:
        passo
    elif buraco == True:
        pule
    elif moeda == True:
        pega
pega    
'''
# Ex. 3 Python
# Utilizando for
for c in range(1, 10):
    print(c)
print('FIM')

# Ex. 3 Python
# Utilizando while
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

# Ex. 4 Python
# Utilizando for
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

# Ex. 4 Python
# Utilizando while
n = 1
while n != 0:
    n = int(input('Digite um valor'))
print('Fim')

# Ex. 5 Python
# Utilizando while
r = 's'
while r == 's':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim') 

# A diferença do for e do while é justamente o limite da iteração. Enquanto o for faz a repetição com base
# em um limite, o while faz a repetição mesmo quando não sabemos o limite da iteração

# Ex. 5 Python
# Utilizando while

n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))