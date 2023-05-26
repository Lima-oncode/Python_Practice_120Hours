from colorama import Fore

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Por favor digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31m O usuário preferiu não informar os dados\033[m')
            return 0
        else:
            return n

def linha(lenn = 30):
    return Fore.LIGHTWHITE_EX + '-' * lenn

def cabecalho(msg):
    print(Fore.LIGHTWHITE_EX + '-' * 30)
    print(Fore.LIGHTWHITE_EX + f'{msg}'.center(30))
    print(Fore.LIGHTWHITE_EX + '-' * 30)
    
def menu():
    cabecalho('Menu principal')
    options = ['Ver usuários cadastrados', 'Cadastrar novo usuário', 'Sair do sistema']
    count = 1
    for op in options:
        print(f'{Fore.YELLOW}{count} - {Fore.CYAN}{op}')
        count += 1
    print(linha())
    choice = leiaint(Fore.YELLOW + 'Digite uma opção: ' + Fore.GREEN)
    return choice