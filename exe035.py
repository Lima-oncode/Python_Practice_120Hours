'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar 
um triângulo
'''

s1 = float(input('Digite o comprimento da primeira reta: '))
s2 = float(input('Digite o comprimento da segunda reta: '))
s3 = float(input('Digite o comprimento da terceira reta: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Esses segmentos formam um triângulo!')
else:
    print('Esses segmentos não formam um triângulo!')


# Resolução do professor

print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')



