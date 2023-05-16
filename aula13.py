# Laços de Repetição (Parte 1)
# Imaginando que um personagem tivesse que andar sobre 10 blocos para pegar uma maçã usamos um laço
# Invés de colocar 10 vezes o comando passo podemos usar o laço para cada bloco o persongem dar o passo
# o ponto de conslusão que é o fim do iterador tem um comando a esquerda para o personagem pegar a maçã
# neste exemplo 'c' é a variável de controle
'''
#Exemplo para compreensão
laço c no intervalo(1,10)
    passo
pega

#Exemplo em python
for c in range(1,10):
    passo
pega


# Contamos agora com um chao que a cada 2 blocos tem um buraco onde o personagem deverá andar 1 bloco e pular
# no seguinte.

#Exemplo para compreensão
laço c no intervalo(0,3)
    passo
    pula
passo
pega

#Exemplo em python
for c in range(0,3):
    passo
    pula
passo
pega

# Considerando a mesma situação porem em um dos blocos tivesse uma moeda

#Exemplo para compreensão
laço c no intervalo(0,3)
    se tiver moeda
        pega
    passo
    pula
passo
pega

#Exemplo em python
for c in range(0,3):
    if == moeda:
        pega
    passo
    pula
passo
pega
'''

#Exemplo em python
for c in range(0, 6):
    print('oi')
print('FIM')

#Exemplo em python
for c in range(0, 7):
    print(c)
print('FIM')

#Exemplo em python
for c in range(6, 0, -1):
    print(c)
print('FIM')

#Exemplo em python
for c in range(0, 7, 2):
    print(c)
print('FIM')

#Exemplo em python
for c in range(0, 9, 4):
    print(c)
print('FIM')

#Exemplo em python
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')

#Exemplo em python
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

#Exemplo em python
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

#Exemplo em python

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
    # s = s + n  é equivalente a  s += n  
print('O somatório de todos os valores foi {}.'.format(s))
