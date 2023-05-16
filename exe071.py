# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Resolução realizada com base na resolução do professor
# O programa consite em iniciar tirando a maior cedula se o valor solicitado for maior ou igual a mesma
# durante essas iterações há um contador e após o total ser menor que a maior cedula há um 'else, if' que faz
# a troca da variavel cedula gradativamente para menos até o fim do valor total 

print('{:^30}'.format( 'BANCO PYTHON S.A' ))

valor = int(input('Qual o valor que você deseja sacar? R$'))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            ceula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0 
        if total == 0:
            break
print('Volte Sempre')