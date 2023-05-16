# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
# perguntar se o usuário quer ou não continuar. No final, mostre
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos


idade = 0
sexo = ''
maioridade = 0
homens = 0
mulheres_20 = 0

print('-'*20)
print('Cadastre uma pessoa')
print('-'*20)

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'mMfF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    else:
        if idade >= 18:
            maioridade += 1
        if sexo in 'mM':
            homens += 1
        if sexo in 'fF' and idade < 20:
            mulheres_20 += 1
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]
        if continuar in 'Ss':
            print('OK! insira os dados do novo cadastro')
        if continuar in 'Nn':
            break
        while continuar not in 'SsNn':
            continuar = str(int(input('Deseja cadastrar mais uma pessoa? [S/N] '))).strip().upper()[0]
print(
f'''Total de pessoas com mais de 18 anos: {maioridade}
Total de homens cadastrados: {homens}
Toal de mulheres com menos de 20 anos: {mulheres_20}''')

# Resolução do professor

tot18 = totH = totM20 = 0

while True: 
    idade = int(input('Idade:'))
    sexo = ''
    while sexo == 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
