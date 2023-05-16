# Crie um programa onde o usuário posssa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares
# em ordem crescente

parimpar = []
par = []
impar = []

for x in range(0, 7):
    n = int(input(f'Digite o {x}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    par.sort()
    impar.sort()
parimpar.append(par)
parimpar.append(impar)
print(f'Os números pares foram: {parimpar[0]}\nOs números ímpares foram: {parimpar[1]}')

# Resolução do professor

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))   
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort
num[1].sort
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')


