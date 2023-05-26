from colorama import Fore

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

def linha(tam = 42):
    return Fore.LIGHTWHITE_EX + '-' * tam

def cabecalho(txt):
    print(Fore.LIGHTWHITE_EX + linha())
    print(Fore.LIGHTWHITE_EX + txt.center(42))
    print(Fore.LIGHTWHITE_EX + linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{Fore.LIGHTYELLOW_EX}{c} - {Fore.CYAN}{item}')
        c += 1
    opc = leiaint2(f'{Fore.YELLOW}Sua opção: {Fore.GREEN}')
    return opc
    

    
    
    
    

        