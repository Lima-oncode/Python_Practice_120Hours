# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[0;31m Por favor digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 'O número digitado foi 0'
        else:
            return f'O número digitado foi {n:.0f}'
            

def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'\033[0;31m Por favor digite um número real!\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 'O número digitado foi 0'
        else:
            return f'O número digitado foi {n:.2f}'

print(leiaint())
print(leiafloat())

# Resolução do professor

def leiaint2(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

num1 = leiaint2('Digite um inteiro: ')

def leiafloat2(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31m Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
num2 = leiafloat2('Digite um real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')
