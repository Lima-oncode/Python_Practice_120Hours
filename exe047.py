# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50
# Lembrando que o resto da divisão de todo número par é == 0 

from time import sleep

print('=-' * 18)
print('Todos os números pares entre 1 e 50')
print('=-' * 18)
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=', ')
        sleep(0.2)
        
# Segunda resolução

par = []
for num in range(1, 51):
    if num % 2 == 0:
        par.append(num)
print(par)

# Terceira resolução

par = list(filter(lambda x: x % 2 == 0, range(1, 51)))
print(par)

# Resolução do professor

for n in range(1,51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

# Segunda resolução do professor
# Neste formato em passos de 2 o código reduz as iterações pera metade, poupando processamento

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')