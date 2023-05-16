# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# tempo_atual = (datetime.date.today())

# Perceba que quando mandamos imprimir o objeto data_nascimento
# o resultado foi uma formatação padrão do python 9999-99-99, 
# isso porque o objeto data é do tipo datetime.data.
# Em resumo strptime, interpreta uma string como um objeto datetime dado um formato correspondente
# strftime Converte/formata objeto para uma string conforme um formato fornecido, 
# no caso strftime(('%d/%m/%Y'))
#data_nascimento = datetime.strptime(nascimento, '%Y').date()
#data_nascimento_format = data_nascimento.strftime('%Y')
#data_atual = (datetime.today())
#data_atual_format = data_atual.strftime('%d/%m/%Y')

nascimento = int(input('Digite seu ano de nascimeto: '))
ano_atual = 2023
idade = ano_atual-nascimento
idade_alistamento = 18

if idade < 18:
    print('Você tem {} anos. Falta {} anos para se alistar ao serviço militar'.format(idade, idade_alistamento-idade))
    ano_alistamento = ano_atual + (idade_alistamento - idade)
    print('Seu alistamento será em {}'.format(ano_alistamento))
elif idade > 18:
    print('Você tem {} anos. Já passou {} anos do tempo de alistamento'.format(idade, idade-idade_alistamento))
    ano_alistamento = ano_atual - (idade - idade_alistamento)
    print('Seu alistamento era para ter sido feito em {}'.format(ano_alistamento))
else:
    print('Você tem {} anos. É a hora de se alistar'.format(idade))

# Resolução do professor

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))







