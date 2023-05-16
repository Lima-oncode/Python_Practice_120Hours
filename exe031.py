'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km
e R$ 0,45 para viagens mais longas
'''

distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    print('O valor total da passagem fica R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor total da passagem fica R${:.2f}'.format(distancia * 0.45))

#resolução do professor

distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco de sua passagem será de R${:.2f}'.format(preco))

# resolução simplificada do professor

distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 
print('E o preco de sua passagem será de R${:.2f}'.format(preco))