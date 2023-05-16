# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acresente, além da idade, com quantos anos a pessoa vai se aposentar
# (Condição para aposentadoria: 35 anos de contribuição)

from datetime import date
from datetime import datetime

dados = {}
ano_atual = date.today().year

while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = ano_atual - int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('Carteira de trabalho (0 caso não tenha): '))
    if dados['ctps'] == 0:
        print('')
        print('_' * 15, 'Validação dos dados', '_' * 15)
        print('')
        for k, v in dados.items():
             print(f'{k} tem o valor : {v}')
        break
    else:
        dados['ano_integracao'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salário: '))
        # ano_atual - integracao = tempo de contribuição
        # (35 - tempo de contruibuição) + idade_atual
        dados['aposentadoria'] = (35 - (ano_atual - dados['ano_integracao'])) + dados['idade']
        print('')
        print('_' * 15, 'Validação dos dados', '_' * 15)
        print('')
        for k, v in dados.items():
            print(f'{k} tem o valor {v}')
        break
    
# Resolução do professor

dado = dict()
dado['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dado['idade'] = datetime.now().year - nasc
dado['ctps']  = int(input('Carteira de trabalho (0 não tem): '))
if dado['ctps'] != 0:
    dado['contratacao'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$'))
    dado['aposentadoria'] = dado['idade'] + ((dado['contratacao'] + 35) - datetime.now().year)
    for k, v in dado.items():
        print(f'{k} tem o valor {v}')


