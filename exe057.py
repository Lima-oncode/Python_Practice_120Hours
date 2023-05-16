#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = 'null'
while sexo not in 'MF':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo not in 'MF':
        print('Digito inválido, digite novamente!')
    elif sexo in 'MF':
        print('Obrigado, tenha um ótimo dia!')

# Resolução do professor

sexo = str(input('Informe seu sexo: [M/F]'))
while sexo not in 'MmFf':
    sexo = int(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))