# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag)

count = soma = 0
while True:
    n = int(input('Digite um número inteiro (999 para finalizar o programa): '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'A soma dos {count} valores foi {soma}!')

# Resolução do professor

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')