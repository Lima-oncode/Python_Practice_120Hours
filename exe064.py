# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor de 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (Desconsiderando o flag)


n = 1
count = 0
n2 = 0

while n != 999:
    n = int(input('Digite um número inteiro ou digite 999 para finalizar o programa: '))
    if n != 999:
        count += 1
        soma = n + n2
        n2 = soma
print('Você digitou {} números e a soma entre eles é {}'.format(count, soma))

# Resolução do professor

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num 
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número e a soma entre eles foi {}.'.format(cont, soma))

