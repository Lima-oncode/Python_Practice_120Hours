# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a sua idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

data_atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
anos = data_atual - nasc

if nasc <= 9:
    print('Nascido em {}. hoje em {} você tem {} anos portanto é um atleta da categoria MIRIM!'.format(nasc,data_atual,anos))
elif nasc > 9 and nasc <= 14:
    print('Nascido em {}. hoje em {} você tem {} anos portanto é um atleta da categoria INFANTIL!'.format(nasc,data_atual,anos))
elif nasc > 14 and nasc <= 19:
    print('Nascido em {}. hoje em {} você tem {} anos portanto é um atleta da categoria JUNIOR!'.format(nasc,data_atual,anos))
elif nasc <= 25:
    print('Nascido em {}. hoje em {} você tem {} anos portanto é um atleta da categoria SÊNIOR!'.format(nasc,data_atual,anos))
else:
    print('Nascido em {}. hoje em {} você tem {} anos portanto é um atleta da categoria MASTER!'.format(nasc,data_atual,anos))
    
# Resolucao do professor

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimeno: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')