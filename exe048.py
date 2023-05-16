# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500

impar = []
for num in range(1, 501, 2):
    if num % 3 == 0:
        impar.append(num)
print('A soma de {} números ímpares de 1 a 500 é {}'.format(len(impar), sum(impar)))

# Resolução do professor
# Na resolução do profesor soma é o acumulador e o cont é o contador
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
        # Equivalente a:
        # cont += 1
        # soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

