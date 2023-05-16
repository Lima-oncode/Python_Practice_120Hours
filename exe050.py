# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

soma = 0

print('=-' * 3, 'Digite seis números inteiros', '=-' * 3)
for x in range(1, 7):
    n = int(input('Digite o {}° número: '.format(x)))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é {}'.format(soma))

# Resolução do professor

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))

