# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

cont = 0
posicao = -1

tupla = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')), 
        int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))

print(tupla)
print('Os números pares são: ', end='')
for x in tupla:
    if x == 9:
        cont +=1
    if x == 3:
        posicao = tupla.index(x)   
    if x % 2 == 0:
        print(f'{x} - ', end='')
print('FIM')
if cont > 0:
    print(f'O número 9 apareceu {cont} vezes')
else:
    print('O número 9 não apareceu na tupla')
if posicao == -1:
    print('O número 3 não apareceu na tupla')
else:
    print(f'o número 3 apareceu na {posicao+1}º posição')

# Resolução do professor

num = (int(input('Digite um número: ')), 
      int(input('Digite outro número: ')), 
      int(input('Digite mais um número: ')), 
      int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')





