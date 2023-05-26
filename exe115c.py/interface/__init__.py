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

def filexists(nome):
    try:
        fl = open(nome, 'rt')
        fl.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        fl = open(nome, 'wt+')
        fl.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
def escrever_arquivo(nome):
    try:
        fl = open(nome, 'wt')
        fl.close
    except:
        print()       
        
def ler_arquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        arq.close()
        
def cadastrar(arq, idade, nome='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escrita do arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()