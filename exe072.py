# Crie uma programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', ' sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

usuario = int(input('Digite um número entre 0 e 20 para ver o número por extenso: '))
while True:
    if usuario > 20 or usuario < 0:
        usuario = int(input('Valor inválido! Digite novamente um número entre 0 e 20 para ver o número por extenso: '))
    else:
        break
print(f'Você digitou o número {contagem[usuario].upper()}')

# Resolução do professor

cont = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', ' sete', 'oito', 'nove',
'dez','onze', 'doze', 'treze', 'quatorze',
'quinze', 'dezeseis', 'dezesete', 'dezoito', 
'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')

