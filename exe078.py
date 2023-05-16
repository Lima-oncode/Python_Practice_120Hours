# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = 0
menor = 0

for v in range(0,5):
    valores.append(int(input(f'Digite o valor na posicao {v}: ')))
print(f'Os valores digitados foram {valores} num total de {len(valores)} algarismos')
maior = max(valores)
menor = min(valores)

for i, v in enumerate(valores):
    if valores[i] == maior:
        posicao_mai = i
        print(f'O maior valor digitado foi {maior} na posicao {posicao_mai}')

for i, v in enumerate(valores):
    if valores[i] == menor:
        posicao_men = i
        print(f'O menor valor digitado foi {menor} na posicao {posicao_men}')

# Resolução do professor:

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]   
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')