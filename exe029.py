'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Digite a velocidade do veículo a ser analizado: '))
multa = ((velocidade - 80) * 7)

if velocidade <= 80:
    print('Fique atento no transito e tenha um bom dia')
else:
    print('Você ultrapassou o limite de velocidade portanto foi multado')
    print('A multa irá custar um total de R${:.2f}'.format(multa))

#Resolução do professor

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
print('Tenha um bom dia! Dirija com segurança!')
