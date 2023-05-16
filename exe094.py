# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
# dicionário e todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo 
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média

dados = {}
pessoas = []
soma = media = 0
apenas_mulheres = ''

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('Digite apenas M ou F na resposta!')
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Digite apenas S ou N na respota!')
    if resposta == 'N':
        break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas' )
media = soma / len(pessoas)
print(f'A média de idade do grupo é {media} anos')
print(f'As mulheres cadastradas foram: ', end='')
for dados in pessoas:
    if dados['sexo'] == 'F':
        print(f'{dados["nome"]} ', end='')
print('')
print(f'As pessoas cadastradas acima da média foram: ', end='')
for dados in pessoas:
    if dados['idade'] >= media:
        print(f'{dados["nome"]}')

# Resolução do professor

galera = []
pessoa = {}
media = soma = 0

while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]  ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
