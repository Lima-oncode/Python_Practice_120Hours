# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex. n = leiaint('Digite um n')

def leiaint():
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            n = int(n)
            print(f'Você digitou o número {n}')
            break
        else:
            print(f'\033[0;31m Você digitou uma informação do tipo {type(n)}! Tente novamente.\033[m')
    return n

leiaint()

# Resolução do professor

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor
        
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

