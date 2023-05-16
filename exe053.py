# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o lobo.

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
consolidado = ''.join(separar)
invertido = consolidado[::-1]

for x in range(1, 2):
    if consolidado == invertido:
        print('A frase é um PALÍNDROMO!')
    else:
        print('A frase NÃO é um PALÍNDROMO!')
print('O inverso de {} é {}'.format(consolidado, invertido))

# Resolução do professor

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é palíndromo!')
