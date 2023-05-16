'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus
dígitos separados.

Ex: 1834
unidade:1
dezena:8
centena:3
milhar:4
'''

'''valor = input('Digite um número entre 0 e 9999: ')

unidade = (valor[0])
dezena = (valor[1])
centena = (valor[2])
milhar = (valor[3])

print(unidade, dezena, centena, milhar)'''

#resolução professor

numero = int(input('Digite um número '))
# tirando o modulo de 10, ou seja pegar o numero digitado dividir por 10 e pegar o resto da divisão nos trás
# o  último digito do valor informado
u = numero // 1 % 10
# no caso, se quisermos o numero decimal, apenas iremos fazer a divisão inteira de 10 e após isso, pegar
# o resto da dvisão de 10 e assim sucessivamente, adicionando um zero a mais na div inteira para cada numero
# a esquerda
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))