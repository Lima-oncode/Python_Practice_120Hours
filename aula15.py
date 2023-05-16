# Interrompendo repetições while

# Exemplo para compreensão
'''
enquanto verdadeiro:
    se chao:
        passo
    se burado:
        pula
    se moeda:
        pega
    se trofeu:
        pula
        interrompa
pega

# Exemplo em python

# while True é um loop infinito 

while true:
    if chao:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega'''

# Exemplo 2 em python

cont =  1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('Acabou')

# Exemplo 3 em python

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

# Detalhes do '.format' em diferentes versões do Python

nome = 'José'
idade = 33
salario = 987.30
print(f'O {nome} tem {idade} anos.') #PYTHON 3.6
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}') #PYTHON 3.6
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3.0
print('O %s tem %d anos.'%(nome, idade)) # PYTHON 2
