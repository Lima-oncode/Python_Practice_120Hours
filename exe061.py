# Refaça o DESAFIO 051, lendo o primeiro termo e razão de um PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while

p1 = int(input('Digite o primeiro termo da P.A: ')) 
r = int(input('Digite a razão da P.A: '))
count = 0

print('Os 10 primeiros termos da P.A são: ')
while count < 10:
    p1 += r
    count += 1
    resultados = print(p1, end=' ')

# Resolução do professor

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

