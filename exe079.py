# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
continuar = ''

while True:
    num = int(input('Digite algum valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    else:
        print('Valor já cadastrado nesta lista, portanto não adicionado.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()   
print(f'Os valores digitados foram: {valores}')

# Resolução do professor

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
