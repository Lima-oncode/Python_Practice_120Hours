# CONDIÇÕES ANINHADAS

'''
carro.siga()
se carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão se carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senão:
    carro.siga()
carro.pare()

carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
elif carro.ré():
    carro.retorne()
else:
    carro.siga()
carro.pare()
'''

#Exemplo 1
#O Elif necessita de um If para funcionar
#O Elif funciona sem a existencia de um Else
nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Larissa, Claudia, Julia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
