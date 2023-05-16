# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
# Será negado.

from time import sleep


print('-='*15)
print('Análise de crédito')
print('-='*15)

casa = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do seu salário: '))
anos_pagamento = float(input('Digite em quantos anos deseja pagar o imóvel: '))
prestacao_mes = (casa / anos_pagamento / 12)
salario30 = (salario * 30 / 100)

print('-='*15)
print('Resumo dos detalhes para análise')
print('-='*15)

print('O valor da casa é R${}.'.format(casa))
print('O seu salário é R${}.'.format(salario))
print('Você deseja pagar o imóvel em {} anos.'.format(anos_pagamento))

print('Estamos Analisando as informações digitadas...')
sleep(5)

if prestacao_mes > salario30:
    print('O empréstimo foi negado devido o valor da prestação ser superior a 30% de sua total')
else:
    print('O empréstimo foi aprovado! para ser pago em {:.0f} anos, com o valor mensal de R${:.2f}'.format(anos_pagamento,prestacao_mes))
print('Obrigado pela preferência!')

### Resolução do professor

casa = float(input('Valor da casa: R$'))
salario = float(input('Saláro do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')







