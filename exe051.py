# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final,
# mostre os 10 primeiros termos dessa progressão

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

for n in range(1, 11):
    a1 = a1 + r
    print('O {}° termo dessa PA é {}'.format(n, a1,))

# Resolução do professor

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='> ')
print('ACABOU')
