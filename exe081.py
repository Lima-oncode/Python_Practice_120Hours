# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma descrescente.
# Se o valor 5 foi digitado está ou não na lista.

valores = []

while True:
    n = (int(input('Digite um valor: ')))
    valores.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort(reverse = True)
print('\n')
print(f'Foram digitados {len(valores)} valores')    
print(f'Os valores digitados ordenado de forma decrescente foram {valores}')
if 5 in valores:
    print('O valor 5 foi digitado na lista')
else:
    print('O valor 5 não foi digitado na lista')

# Resolução do professor

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] 
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

