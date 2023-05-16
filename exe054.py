# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import date

count_maior = 0
count_menor = 0

for ano in range(1,8):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(ano)))
    atual = date.today().year
    idade = atual - nasc
    if idade < 21:
        count_menor += 1
    else:
        count_maior += 1
print('{} pessoas são de maiores e {} pessoas não atingiram a maioridade'.format(count_maior, count_menor))

# Resolução do professor

from datetime import date

atual = date.today().year
tot_maior = 0
tot_menor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(tot_maior))
print('E também tivemos {} pessoas menores de idade'.format(tot_menor))  
