# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo 
# usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-'*35)
    for n in range(1, 11):
        if n == 11:
            break
        print(f'{valor} X {n} = {n * valor}')
    print('-'*35)
print('Programa Finalizado!')

# Resolução do professor

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
