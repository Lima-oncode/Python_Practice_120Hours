# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

count = soma = maior = menor = 0
s_n = 'S'

while s_n in 'SsNn':  
    if s_n in 'Ss':
        n = int(input('Digite um valor inteiro: '))
        count += 1
        soma += n
        if count == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
            if n == maior and n == menor:
                n = maior = menor
        s_n = str(input('Deseja prosseguir com o programa [S/N]: ')).strip().upper()[0]
        if s_n in 'Nn':
            print('Apurando os dados . . .')
            print('_'*90)
            break
media = soma / count
print('Você digitou {} números, a soma entre eles é {}, a média entre eles é de {:.2f}'.format(count, soma, media))
if n == maior == menor:
    print('Não existe maior nem menor valor pois todos são equivalentes')
else:
    print('o maior valor lido foi {} e o menor valor lido foi {}'.format(maior, menor))

# Resolução do professor

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        resp = int(input('Digite um número: '))
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
