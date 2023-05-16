# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: Todos os lados diferentes

s1 = float(input('Digite o comprimento da primeira reta: '))
s2 = float(input('Digite o comprimento da segunda reta: '))
s3 = float(input('Digite o comprimento da terceira reta: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Esses segmentos formam um triângulo!')
    if s1 == s2 and s2 == s3:
        print('O tipo do triângulo formado é Equilátero. Pois todos os lados são iguais.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('O tipo do triângulo formado é Isósceles. Pois dois lados são iguais.')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('O tipo do triângulo formado é Escaleno. Pois todos os lados são diferentes.')
else:
    print('Esses segmentos não formam um triângulo!')

# Resolução do professor

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')  
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')