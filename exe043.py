# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('========= CÁLCULO DE IMC =========')

peso = float(input('Digite o valor de seu peso: '))
altura = float(input('Digite o valor de sua altura: '))
altura_quadrado = altura * altura
imc = (peso / altura_quadrado)

if imc < 18.50:
    print('O seu IMC está em {:.1f} portando você está abaixo do peso!'.format(imc))
elif imc < 25:
    print('O seu IMC está em {:.1f} portando você está com o peso ideal!'.format(imc))
elif imc < 30:
    print('O seu IMC está em {:.1f} portando você está com sobrepeso!'.format(imc))
elif imc < 40:
    print('O seu IMC está em {:.1f} portando você está com obesidade!'.format(imc))
else:
    print('O seu IMC está em {:.1f} portando você está com obesidade mórbida!'.format(imc))

# Resolução do professor

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
