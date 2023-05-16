# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista e mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas (> 100 kg)
# Uma listagem com as pessoas mais leves (< 70kg)

dados = []
relatorio = []
maispesado = []
menospesado = []
cont  = 0

while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    relatorio.append(dados[:])
    dados.clear()
    cont += 1
    proximo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if 'N' in proximo:
        break
print(relatorio)


for x in relatorio:
     if x[1] <= 70:
         menospesado.append(x)
     if x[1] >= 100:
         maispesado.append(x)
    
min = min(menospesado)
max = max(maispesado)

print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {max[1]} Kg. Pesagem de {maispesado[0][0]}')
print(f'O menor peso foi de {min[1]} Kg. Pesagem de {menospesado[0][0]}')

# Resolução do professor

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Ao todo voce cadastrou {len(princ)} pessoas ')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men}. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}') 