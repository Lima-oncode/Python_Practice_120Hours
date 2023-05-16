#Teoria

''' Em uma situação onde um carro pode seguir dois caminhos para chegar o mesmo destino o professor
exemplificou da seguite maneira usando os métodos
'''
'''
carro.siga()
    if carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga()
        carro.direita()
        carro.esquerda()
        carro.siga()
        carro.direita()
        carro.siga()
    else
        carro.siga()
        carro.esquerda()
        carro.siga()
        carro.esquerda()
        carro.siga()
carro.pare()
'''

#Explicação de condição (sempre lembrando dos dois pontos após o if e o else)

'''
if carro.esquerda():
    bloco True
else:
    bloco False
'''

#Exemplo 2:

tempo = int(input('Quantos anos tem o seu carro? '))

if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# Condição simplificada

tempo = int(input('Quantos anos tem o seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')